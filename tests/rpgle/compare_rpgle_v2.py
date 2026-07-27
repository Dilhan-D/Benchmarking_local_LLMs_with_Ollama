#!/usr/bin/env python3
"""
Comparateur CLLE - Ollama Granite Test Series
Compare #Xtest.clle (questions) vs #resultX.clle (réponses Ollama)

v4 : suppression des commentaires en fin de ligne (pas seulement les
     lignes 100% commentaire) + indentation toujours ignorée (sans
     valeur syntaxique en RPGLE/CL/COBOL) + casse ignorée par défaut.
"""


import os
import csv
import json
import re
import difflib
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv


load_dotenv(dotenv_path=Path(__file__).parent / ".env")


LANGAGE         = os.environ["LANGAGE"]
EXTENSION       = os.environ["EXTENSION"]
DIR_QUESTIONS   = Path(__file__).parent / os.environ["DIR_QUESTIONS"]
DIR_REPONSES    = Path(__file__).parent / os.environ["DIR_REPONSES"]
DIR_RESULTATS   = Path(__file__).parent / os.environ["DIR_RESULTATS"]
NOM_RAPPORT     = os.environ["NOM_RAPPORT"]

# Langages IBM i insensibles à la casse et à l'indentation : on force
# ces options à true par défaut (surchargeables explicitement via .env).
IGNORER_CASSE   = os.environ.get("IGNORER_CASSE", "true").lower()        == "true"
IGNORER_ESPACES = os.environ.get("IGNORER_ESPACES", "true").lower()      == "true"
IGNORER_VIDES   = os.environ.get("IGNORER_LIGNES_VIDES", "true").lower() == "true"

MODELE_LLM       = os.environ.get("MODELE_LLM", "granite4.1:8b")
GENERER_MARKDOWN = os.environ.get("GENERER_MARKDOWN", "true").lower() == "true"

# Ignore les commentaires (lignes entières ET fin de ligne) lors de la comparaison.
IGNORER_COMMENTAIRES = os.environ.get("IGNORER_COMMENTAIRES", "true").lower() == "true"

DIR_RESULTATS.mkdir(parents=True, exist_ok=True)


# ============================================================
# EXTRACTION / NORMALISATION INTELLIGENTE DU CODE
# ============================================================

BLOC_MARKDOWN_RE = re.compile(
    r"```[ \t]*([a-zA-Z0-9_+-]*)[ \t]*\n(.*?)```",
    re.DOTALL
)


def extraire_code_depuis_reponse(texte_brut):
    blocs = BLOC_MARKDOWN_RE.findall(texte_brut)

    if blocs:
        morceaux = [contenu.strip("\n") for _, contenu in blocs]
        return "\n\n".join(morceaux), True

    lignes = texte_brut.splitlines()
    phrases_explicatives = re.compile(
        r"^\s*(voici|ce programme|explication|remarque|note\s*:|analyse|"
        r"le code|correction|résumé|summary|explanation|here is|this program)",
        re.IGNORECASE
    )
    lignes_gardees = [l for l in lignes if not phrases_explicatives.match(l)]
    return "\n".join(lignes_gardees).strip(), False


# ============================================================
# FILTRAGE COMMENTAIRES (bloc + fin de ligne) / LIGNES VIDES
# ============================================================

def supprimer_commentaires_bloc(texte):
    """Supprime les blocs /* ... */ multi-lignes."""
    return re.sub(r"/\*.*?\*/", "", texte, flags=re.DOTALL)


def supprimer_commentaire_fin_ligne(ligne):
    """
    Supprime un commentaire en fin de ligne (// ... ou /* ... */ résiduel),
    en protégeant le contenu des chaînes littérales entre quotes simples
    pour ne pas tronquer un '//' ou '/*' présent dans une valeur.
    """
    dernier_quote = ligne.rfind("'")
    zone_protegee  = ligne[:dernier_quote + 1] if dernier_quote != -1 else ""
    zone_a_traiter = ligne[len(zone_protegee):]

    zone_a_traiter = re.sub(r"//.*$", "", zone_a_traiter)
    zone_a_traiter = re.sub(r"/\*.*?(\*/)?$", "", zone_a_traiter)

    return zone_protegee + zone_a_traiter


def est_ligne_commentaire(ligne):
    """Détecte une ligne 100% commentaire (après strip)."""
    l = ligne.strip()
    if not l:
        return False
    if l.startswith("//"):
        return True
    if l.startswith("/*") or l.endswith("*/"):
        return True
    if l.startswith("*") and not l.startswith("**"):
        return True
    return False


def nettoyer_code(texte):
    """
    Pipeline de normalisation appliqué à l'input ET à l'output avant
    comparaison :
    1. Suppression des blocs /* ... */ multi-lignes.
    2. Découpage en lignes.
    3. Suppression des lignes 100% commentaire, PUIS suppression des
       commentaires en fin de ligne restants (ex: 'code; // note').
    4. Strip systématique : l'indentation est ignorée car sans valeur
       syntaxique en RPGLE/CL/COBOL.
    5. Suppression des lignes devenues vides.
    """
    texte = supprimer_commentaires_bloc(texte)
    lignes = texte.splitlines()

    lignes_utiles = []
    for l in lignes:
        l = l.rstrip('\n')

        if IGNORER_COMMENTAIRES:
            if est_ligne_commentaire(l):
                continue
            l = supprimer_commentaire_fin_ligne(l)

        l = l.strip()  # indentation toujours ignorée

        if IGNORER_VIDES and l == '':
            continue

        lignes_utiles.append(l)

    return lignes_utiles


def normaliser_ligne(ligne):
    """
    Normalisation finale avant comparaison :
    - strip (indentation ignorée)
    - casse ignorée par défaut (RPG/CL/COBOL insensibles à la casse)
    - espaces internes multiples réduits à un seul
    """
    ligne = ligne.strip()
    if IGNORER_CASSE:
        ligne = ligne.lower()
    if IGNORER_ESPACES:
        ligne = ' '.join(ligne.split())
    return ligne


def lire_fichier(chemin):
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"  ATTENTION: fichier introuvable -> {chemin}")
        return ""


# ============================================================
# COMPARAISON PAR ALIGNEMENT RÉEL (difflib)
# ============================================================

def comparer(lignes1, lignes2):
    lignes1_norm = [normaliser_ligne(l) for l in lignes1]
    lignes2_norm = [normaliser_ligne(l) for l in lignes2]

    sm = difflib.SequenceMatcher(a=lignes1_norm, b=lignes2_norm, autojunk=False)

    nb_identiques = 0
    nb_modifiees  = 0
    nb_ajoutees   = 0
    nb_supprimees = 0
    differences   = []

    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            nb_identiques += (i2 - i1)
        elif tag == 'replace':
            n = max(i2 - i1, j2 - j1)
            for k in range(n):
                avant = lignes1[i1 + k] if (i1 + k) < i2 else ''
                apres = lignes2[j1 + k] if (j1 + k) < j2 else ''
                nb_modifiees += 1
                differences.append({'ligne': i1 + k + 1, 'type': 'MODIFIEE', 'avant': avant, 'apres': apres})
        elif tag == 'delete':
            for k in range(i1, i2):
                nb_supprimees += 1
                differences.append({'ligne': k + 1, 'type': 'SUPPRIMEE', 'avant': lignes1[k], 'apres': ''})
        elif tag == 'insert':
            for k in range(j1, j2):
                nb_ajoutees += 1
                differences.append({'ligne': i1 + 1, 'type': 'AJOUTEE', 'avant': '', 'apres': lignes2[k]})

    total_ref  = len(lignes1) if lignes1 else (len(lignes2) if lignes2 else 1)
    similarite = round((nb_identiques / total_ref) * 100, 2) if total_ref else 100.0

    return {
        'nb_identiques' : nb_identiques,
        'nb_modifiees'  : nb_modifiees,
        'nb_ajoutees'   : nb_ajoutees,
        'nb_supprimees' : nb_supprimees,
        'nb_diff'       : nb_modifiees + nb_ajoutees + nb_supprimees,
        'similarite'    : similarite,
        'total_entree'  : len(lignes1),
        'total_sortie'  : len(lignes2),
    }, differences


def ecrire_rapport_txt(num, stats, differences, date_exec, num_exec, chemin, extraction_ok):
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write(f"   RAPPORT DE COMPARAISON - {LANGAGE.upper()} TEST #{num}\n")
        f.write("=" * 60 + "\n")
        f.write(f"  Date d'exécution  : {date_exec}\n")
        f.write(f"  Numéro exécution  : #{num_exec}\n")
        f.write(f"  Langage           : {LANGAGE.upper()}\n")
        f.write(f"  Modèle            : {MODELE_LLM}\n")
        f.write(f"  Entrée            : #{num}test{EXTENSION}\n")
        f.write(f"  Réponse Granite   : #result{num}{EXTENSION}\n")
        f.write(f"  Extraction code   : {'bloc Markdown' if extraction_ok else 'heuristique (pas de bloc détecté)'}\n")
        f.write(f"  Options actives   : casse_ignoree={IGNORER_CASSE} | espaces_ignores={IGNORER_ESPACES} | "
                f"vides_ignorees={IGNORER_VIDES} | commentaires_ignores={IGNORER_COMMENTAIRES}\n")
        f.write(f"  Méthode comparaison : alignement difflib (SequenceMatcher)\n")
        f.write("-" * 60 + "\n")
        f.write(f"  Total lignes entrée (utiles) : {stats['total_entree']}\n")
        f.write(f"  Total lignes sortie (utiles) : {stats['total_sortie']}\n")
        f.write("-" * 60 + "\n")
        f.write(f"  Lignes identiques    : {stats['nb_identiques']}\n")
        f.write(f"  Lignes modifiées     : {stats['nb_modifiees']}\n")
        f.write(f"  Lignes ajoutées      : {stats['nb_ajoutees']}\n")
        f.write(f"  Lignes supprimées    : {stats['nb_supprimees']}\n")
        f.write(f"  Total différences    : {stats['nb_diff']}\n")
        f.write(f"  Similarité globale   : {stats['similarite']}%\n")
        f.write("=" * 60 + "\n\n")

        if differences:
            f.write("DÉTAIL DES DIFFÉRENCES :\n")
            f.write("-" * 60 + "\n")
            for d in differences:
                if d['type'] == 'MODIFIEE':
                    f.write(f"  ~ Ligne {d['ligne']:4} | AVANT : {d['avant']}\n")
                    f.write(f"             | APRÈS : {d['apres']}\n\n")
                elif d['type'] == 'AJOUTEE':
                    f.write(f"  + Ligne {d['ligne']:4} | AJOUT : {d['apres']}\n\n")
                elif d['type'] == 'SUPPRIMEE':
                    f.write(f"  - Ligne {d['ligne']:4} | SUPPR : {d['avant']}\n\n")
        else:
            f.write("  Aucune différence. Fichiers identiques (hors commentaires/indentation/casse).\n")


def ecrire_rapport_markdown(num, stats, differences, date_exec, num_exec, chemin,
                             code_original, code_extrait, extraction_ok):
    lang_fence = {
        "rpg": "rpg", "cl": "cl", "clle": "cl",
        "sql": "sql", "cobol": "cobol"
    }.get(LANGAGE.lower(), "")

    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(f"# Rapport de comparaison — {LANGAGE.upper()} — Test #{num}\n\n")

        f.write("## Informations générales\n\n")
        f.write("| Champ | Valeur |\n")
        f.write("|---|---|\n")
        f.write(f"| Test | #{num} |\n")
        f.write(f"| Langage IBM i | {LANGAGE.upper()} |\n")
        f.write(f"| Date d'exécution | {date_exec} |\n")
        f.write(f"| Numéro d'exécution | #{num_exec} |\n")
        f.write(f"| Modèle utilisé | {MODELE_LLM} |\n")
        f.write(f"| Lignes input (utiles) | {stats['total_entree']} |\n")
        f.write(f"| Lignes output (utiles) | {stats['total_sortie']} |\n")
        f.write(f"| Méthode d'extraction | {'Bloc Markdown détecté' if extraction_ok else 'Heuristique (aucun bloc trouvé)'} |\n")
        f.write(f"| Méthode de comparaison | Alignement difflib (SequenceMatcher) |\n")
        f.write(f"| Commentaires ignorés | {IGNORER_COMMENTAIRES} |\n")
        f.write(f"| Casse ignorée | {IGNORER_CASSE} |\n")
        f.write(f"| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |\n\n")

        f.write("## Statistiques de comparaison\n\n")
        f.write("| Métrique | Valeur |\n")
        f.write("|---|---|\n")
        f.write(f"| Lignes identiques | {stats['nb_identiques']} |\n")
        f.write(f"| Lignes modifiées | {stats['nb_modifiees']} |\n")
        f.write(f"| Lignes ajoutées | {stats['nb_ajoutees']} |\n")
        f.write(f"| Lignes supprimées | {stats['nb_supprimees']} |\n")
        f.write(f"| Total différences | {stats['nb_diff']} |\n")
        f.write(f"| **Similarité globale** | **{stats['similarite']}%** |\n\n")

        f.write("## Différences détectées\n\n")
        if differences:
            f.write("| Ligne | Type | Avant | Après |\n")
            f.write("|---|---|---|---|\n")
            for d in differences:
                avant = d['avant'].replace('|', '\\|') if d['avant'] else ''
                apres = d['apres'].replace('|', '\\|') if d['apres'] else ''
                f.write(f"| {d['ligne']} | {d['type']} | `{avant}` | `{apres}` |\n")
            f.write("\n")
        else:
            f.write("_Aucune différence significative (hors commentaires/indentation/casse)._\n\n")

        f.write("## Code original (input)\n\n")
        f.write(f"```{lang_fence}\n{code_original}\n```\n\n")

        f.write("## Réponse Granite — code extrait (output normalisé)\n\n")
        f.write(f"```{lang_fence}\n{code_extrait}\n```\n\n")


def get_compteur():
    compteur_path = DIR_RESULTATS / "compteur.json"
    if compteur_path.exists():
        with open(compteur_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {"executions": 0, "historique": []}

    data["executions"] += 1
    data["historique"].append({
        "execution" : data["executions"],
        "date"      : datetime.now().strftime("%Y-%m-%d")
    })

    with open(compteur_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return data["executions"]


def main():
    date_exec = datetime.now().strftime("%Y-%m-%d")
    num_exec  = get_compteur()

    print("=" * 60)
    print(f"   COMPARATEUR {LANGAGE.upper()} - GRANITE TEST SERIES")
    print(f"   Exécution #{num_exec} - {date_exec}")
    print("=" * 60)
    print(f"  Questions : {DIR_QUESTIONS.resolve()}")
    print(f"  Réponses  : {DIR_REPONSES.resolve()}")
    print(f"  Résultats : {DIR_RESULTATS.resolve()}")
    print(f"  Commentaires ignorés : {IGNORER_COMMENTAIRES} | Casse ignorée : {IGNORER_CASSE}")
    print("=" * 60)

    fichiers_test = sorted(DIR_QUESTIONS.glob(f"#*test{EXTENSION}"))

    if not fichiers_test:
        print(f"\n  Aucun fichier trouvé (#*test{EXTENSION}) dans :")
        print(f"  {DIR_QUESTIONS.resolve()}")
        return

    resultats_globaux = []

    for fichier_test in fichiers_test:
        num             = fichier_test.stem.replace('#', '').replace('test', '')
        fichier_reponse = DIR_REPONSES / f"#result{num}{EXTENSION}"

        print(f"\n  Test #{num}")
        print(f"    Entrée  : {fichier_test.name}")
        print(f"    Réponse : {fichier_reponse.name}")

        contenu_test    = lire_fichier(fichier_test)
        contenu_reponse = lire_fichier(fichier_reponse)

        code_extrait, extraction_ok = extraire_code_depuis_reponse(contenu_reponse)

        lignes_test    = nettoyer_code(contenu_test)
        lignes_reponse = nettoyer_code(code_extrait)

        stats, differences = comparer(lignes_test, lignes_reponse)

        rapport_txt = DIR_RESULTATS / f"#diff{num}_rapport.txt"
        ecrire_rapport_txt(num, stats, differences, date_exec, num_exec, rapport_txt, extraction_ok)

        if GENERER_MARKDOWN:
            rapport_md = DIR_RESULTATS / f"#diff{num}_rapport.md"
            ecrire_rapport_markdown(
                num, stats, differences, date_exec, num_exec, rapport_md,
                contenu_test, code_extrait, extraction_ok
            )

        print(f"    Extraction  : {'bloc Markdown' if extraction_ok else 'heuristique'}")
        print(f"    Similarité  : {stats['similarite']}%")
        print(f"    Différences : {stats['nb_diff']} "
              f"({stats['nb_modifiees']} modif / "
              f"{stats['nb_ajoutees']} ajout / "
              f"{stats['nb_supprimees']} suppr)")
        print(f"    Rapport txt : {rapport_txt.name}")
        if GENERER_MARKDOWN:
            print(f"    Rapport md  : {rapport_md.name}")

        resultats_globaux.append({
            'execution'         : num_exec,
            'date'              : date_exec,
            'langage'           : LANGAGE,
            'test'              : f"#{num}",
            'fichier_entree'    : fichier_test.name,
            'fichier_reponse'   : fichier_reponse.name,
            'lignes_entree'     : stats['total_entree'],
            'lignes_sortie'     : stats['total_sortie'],
            'identiques'        : stats['nb_identiques'],
            'modifiees'         : stats['nb_modifiees'],
            'ajoutees'          : stats['nb_ajoutees'],
            'supprimees'        : stats['nb_supprimees'],
            'total_diff'        : stats['nb_diff'],
            'similarite'        : stats['similarite'],
            'extraction_bloc_md': extraction_ok,
            'differences'       : differences
        })

    csv_path   = DIR_RESULTATS / f"{NOM_RAPPORT}.csv"
    csv_fields = [
        'execution', 'date', 'langage', 'test',
        'fichier_entree', 'fichier_reponse',
        'lignes_entree', 'lignes_sortie',
        'identiques', 'modifiees', 'ajoutees',
        'supprimees', 'total_diff', 'similarite',
        'extraction_bloc_md'
    ]

    if csv_path.exists():
        with open(csv_path, 'r', encoding='utf-8') as f:
            premiere_ligne = f.readline().strip()
        header_existant = premiere_ligne.split(';')
        if header_existant != csv_fields:
            print(f"  ATTENTION: schema CSV different detecte -> reinitialisation de {csv_path.name}")
            csv_path.unlink()

    mode_csv = 'a' if csv_path.exists() else 'w'
    with open(csv_path, mode_csv, newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields, delimiter=';')
        if mode_csv == 'w':
            writer.writeheader()
        for r in resultats_globaux:
            writer.writerow({k: r[k] for k in csv_fields})

    json_path = DIR_RESULTATS / f"{NOM_RAPPORT}.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({
            'execution' : num_exec,
            'date'      : date_exec,
            'langage'   : LANGAGE,
            'resultats' : resultats_globaux
        }, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 60)
    print(f"  Exécution #{num_exec} terminée le {date_exec}")
    print(f"  CSV  : {csv_path.name}")
    print(f"  JSON : {json_path.name}")
    print("=" * 60)


if __name__ == '__main__':
    main()
