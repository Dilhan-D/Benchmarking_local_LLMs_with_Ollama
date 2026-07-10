#!/usr/bin/env python3
"""
Comparateur CLLE - Ollama Granite Test Series
Compare #Xtest.clle (questions) vs #resultX.clle (réponses Ollama)

v2 : ajout normalisation intelligente (extraction code depuis blocs Markdown)
     + génération de rapports Markdown lisibles dans VS Code
"""


import os
import csv
import json
import re
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
IGNORER_CASSE   = os.environ["IGNORER_CASSE"].lower()        == "true"
IGNORER_ESPACES = os.environ["IGNORER_ESPACES"].lower()      == "true"
IGNORER_VIDES   = os.environ["IGNORER_LIGNES_VIDES"].lower() == "true"

# Nom du modèle utilisé (pour les rapports). Peut être surchargé via .env : MODELE_LLM=granite4.1:8b
MODELE_LLM      = os.environ.get("MODELE_LLM", "granite4.1:8b")

# Génération des rapports Markdown en plus du .txt (activable via .env : GENERER_MARKDOWN=true)
GENERER_MARKDOWN = os.environ.get("GENERER_MARKDOWN", "true").lower() == "true"


DIR_RESULTATS.mkdir(parents=True, exist_ok=True)


# ============================================================
# EXTRACTION / NORMALISATION INTELLIGENTE DU CODE
# ============================================================

# Détecte les blocs ```<lang> ... ``` (lang optionnel, insensible à la casse)
BLOC_MARKDOWN_RE = re.compile(
    r"```[ \t]*([a-zA-Z0-9_+-]*)[ \t]*\n(.*?)```",
    re.DOTALL
)

# Alias de langage acceptés pour un match "safe" (informatif seulement)
ALIAS_LANGAGE = {
    "rpg": ["rpg", "rpgle", "rpgiv", "rpgfree", "sqlrpgle"],
    "cl":  ["cl", "clle", "cmd"],
    "sql": ["sql", "db2"],
    "cobol": ["cobol", "cbl"],
}


def extraire_code_depuis_reponse(texte_brut):
    """
    Extrait uniquement le code utile d'une réponse LLM :
    - Si des blocs ```...``` sont présents, on concatène leur contenu
      (on ignore le texte d'explication autour).
    - Sinon, on tente une heuristique de repli : on supprime les lignes
      qui ressemblent à des phrases d'explication en langage naturel
      (terminant par '.', ':', commençant par des tournures type
      "Voici", "Ce programme", "Explication", etc.)
    """
    blocs = BLOC_MARKDOWN_RE.findall(texte_brut)

    if blocs:
        morceaux = [contenu.strip("\n") for _, contenu in blocs]
        code_extrait = "\n\n".join(morceaux)
        return code_extrait, True  # True = extraction via bloc Markdown

    # Repli heuristique si aucun bloc Markdown détecté
    lignes = texte_brut.splitlines()
    phrases_explicatives = re.compile(
        r"^\s*(voici|ce programme|explication|remarque|note\s*:|analyse|"
        r"le code|correction|résumé|summary|explanation|here is|this program)",
        re.IGNORECASE
    )
    lignes_gardees = []
    for l in lignes:
        if phrases_explicatives.match(l):
            continue
        # ligne quasi vide entourée de texte narratif : on la garde par prudence
        lignes_gardees.append(l)

    return "\n".join(lignes_gardees).strip(), False  # False = repli heuristique


def normaliser_ligne(ligne):
    ligne = ligne.strip()
    if IGNORER_CASSE:
        ligne = ligne.lower()
    if IGNORER_ESPACES:
        ligne = ' '.join(ligne.split())
    return ligne


def lire_fichier(chemin):
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            contenu = f.read()
        return contenu
    except FileNotFoundError:
        print(f"  ATTENTION: fichier introuvable -> {chemin}")
        return ""


def contenu_vers_lignes(contenu):
    lignes = [l.rstrip('\n') for l in contenu.splitlines()]
    if IGNORER_VIDES:
        lignes = [l for l in lignes if l.strip() != '']
    return lignes


def comparer(lignes1, lignes2):
    nb_identiques = 0
    nb_modifiees  = 0
    nb_ajoutees   = 0
    nb_supprimees = 0
    differences   = []

    max_lignes = max(len(lignes1), len(lignes2)) if (lignes1 or lignes2) else 0

    for i in range(max_lignes):
        if i >= len(lignes2):
            nb_supprimees += 1
            differences.append({'ligne': i+1, 'type': 'SUPPRIMEE', 'avant': lignes1[i], 'apres': ''})
        elif i >= len(lignes1):
            nb_ajoutees += 1
            differences.append({'ligne': i+1, 'type': 'AJOUTEE', 'avant': '', 'apres': lignes2[i]})
        elif normaliser_ligne(lignes1[i]) == normaliser_ligne(lignes2[i]):
            nb_identiques += 1
        else:
            nb_modifiees += 1
            differences.append({'ligne': i+1, 'type': 'MODIFIEE', 'avant': lignes1[i], 'apres': lignes2[i]})

    total      = max(len(lignes1), len(lignes2)) if (lignes1 or lignes2) else 1
    similarite = round((nb_identiques / total) * 100, 2)

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
        f.write(f"  Options actives   : casse={IGNORER_CASSE} | espaces={IGNORER_ESPACES} | vides={IGNORER_VIDES}\n")
        f.write("-" * 60 + "\n")
        f.write(f"  Total lignes entrée  : {stats['total_entree']}\n")
        f.write(f"  Total lignes sortie  : {stats['total_sortie']}\n")
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
            f.write("  Aucune différence. Fichiers identiques.\n")


def ecrire_rapport_markdown(num, stats, differences, date_exec, num_exec, chemin,
                             code_original, code_extrait, extraction_ok):
    """
    Génère un rapport .md lisible directement dans VS Code
    (aperçu Markdown natif : Ctrl+Shift+V).
    """
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
        f.write(f"| Lignes input | {stats['total_entree']} |\n")
        f.write(f"| Lignes output (extrait) | {stats['total_sortie']} |\n")
        f.write(f"| Méthode d'extraction | {'Bloc Markdown détecté' if extraction_ok else 'Heuristique (aucun bloc trouvé)'} |\n\n")

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
            f.write("_Aucune différence. Fichiers identiques._\n\n")

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
        "date"      : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    with open(compteur_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return data["executions"]


def main():
    date_exec = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    num_exec  = get_compteur()

    print("=" * 60)
    print(f"   COMPARATEUR {LANGAGE.upper()} - GRANITE TEST SERIES")
    print(f"   Exécution #{num_exec} - {date_exec}")
    print("=" * 60)
    print(f"  Questions : {DIR_QUESTIONS.resolve()}")
    print(f"  Réponses  : {DIR_REPONSES.resolve()}")
    print(f"  Résultats : {DIR_RESULTATS.resolve()}")
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

        # --- Normalisation intelligente de la réponse Granite ---
        code_extrait, extraction_ok = extraire_code_depuis_reponse(contenu_reponse)

        lignes_test    = contenu_vers_lignes(contenu_test)
        lignes_reponse = contenu_vers_lignes(code_extrait)

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
