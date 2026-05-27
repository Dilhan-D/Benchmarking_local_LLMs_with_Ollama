#!/usr/bin/env python3
"""
Comparateur RPGLE - Ollama Granite Test Series
"""

import os
import csv
import json
from pathlib import Path
from dotenv import load_dotenv

# ============================================================
# CHARGEMENT .env
# ============================================================
load_dotenv()

BASE_DIR        = Path(os.getenv("BASE_DIR",     "../rpgle_questions_before_finetune"))
DIR_QUESTIONS   = Path(os.getenv("DIR_QUESTIONS", "../rpgle_questions_before_finetune/questions_before_finetune"))
DIR_REPONSES    = Path(os.getenv("DIR_REPONSES",  "../rpgle_questions_before_finetune/answers_before_finetune"))
DIR_RESULTATS   = Path(os.getenv("DIR_RESULTATS", "./rpgle_test_before_finetune"))
NOM_RAPPORT     = os.getenv("NOM_RAPPORT", "synthese_comparaison")
IGNORER_CASSE   = os.getenv("IGNORER_CASSE",        "false").lower() == "true"
IGNORER_ESPACES = os.getenv("IGNORER_ESPACES",      "false").lower() == "true"
IGNORER_VIDES   = os.getenv("IGNORER_LIGNES_VIDES", "true").lower()  == "true"

DIR_RESULTATS.mkdir(parents=True, exist_ok=True)


# ============================================================
# FONCTIONS
# ============================================================

def lire_fichier(chemin):
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            lignes = [l.rstrip('\n') for l in f.readlines()]
        if IGNORER_VIDES:
            lignes = [l for l in lignes if l.strip() != '']
        return lignes
    except FileNotFoundError:
        print(f"  ATTENTION: fichier introuvable -> {chemin}")
        return []


def normaliser(ligne):
    """Applique les options d'ignorance selon .env"""
    if IGNORER_CASSE:
        ligne = ligne.lower()
    if IGNORER_ESPACES:
        ligne = ' '.join(ligne.split())
    return ligne


def comparer(lignes1, lignes2):
    nb_identiques  = 0
    nb_modifiees   = 0
    nb_ajoutees    = 0
    nb_supprimees  = 0
    differences    = []

    max_lignes = max(len(lignes1), len(lignes2)) if (lignes1 or lignes2) else 0

    for i in range(max_lignes):
        if i >= len(lignes2):
            nb_supprimees += 1
            differences.append({
                'ligne': i + 1, 'type': 'SUPPRIMEE',
                'avant': lignes1[i], 'apres': ''
            })
        elif i >= len(lignes1):
            nb_ajoutees += 1
            differences.append({
                'ligne': i + 1, 'type': 'AJOUTEE',
                'avant': '', 'apres': lignes2[i]
            })
        elif normaliser(lignes1[i]) == normaliser(lignes2[i]):
            nb_identiques += 1
        else:
            nb_modifiees += 1
            differences.append({
                'ligne': i + 1, 'type': 'MODIFIEE',
                'avant': lignes1[i], 'apres': lignes2[i]
            })

    total      = max(len(lignes1), len(lignes2))
    similarite = round((nb_identiques / total) * 100, 2) if total > 0 else 0

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


def ecrire_rapport_txt(num, stats, differences, chemin):
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write(f"   RAPPORT DE COMPARAISON - TEST #{num}\n")
        f.write("=" * 60 + "\n")
        f.write(f"  Entrée  : #{num}test.rpgle\n")
        f.write(f"  Réponse : #result{num}.rpgle\n")
        f.write(f"  Options : casse={IGNORER_CASSE} | espaces={IGNORER_ESPACES} | vides={IGNORER_VIDES}\n")
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


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("   COMPARATEUR RPGLE - GRANITE TEST SERIES")
    print("=" * 60)
    print(f"  Questions : {DIR_QUESTIONS}")
    print(f"  Réponses  : {DIR_REPONSES}")
    print(f"  Résultats : {DIR_RESULTATS}")
    print("=" * 60)

    fichiers_test = sorted(DIR_QUESTIONS.glob("#*test.rpgle"))

    if not fichiers_test:
        print(f"  Aucun fichier trouvé dans : {DIR_QUESTIONS}")
        return

    resultats_globaux = []

    for fichier_test in fichiers_test:
        nom = fichier_test.stem
        num = nom.replace('#', '').replace('test', '')
        fichier_reponse = DIR_REPONSES / f"#result{num}.rpgle"

        print(f"\n  Test #{num}")

        lignes_test    = lire_fichier(fichier_test)
        lignes_reponse = lire_fichier(fichier_reponse)
        stats, differences = comparer(lignes_test, lignes_reponse)

        # Rapport .txt détaillé
        rapport_txt = DIR_RESULTATS / f"#diff{num}_rapport.txt"
        ecrire_rapport_txt(num, stats, differences, rapport_txt)

        print(f"    Similarité  : {stats['similarite']}%")
        print(f"    Différences : {stats['nb_diff']} "
              f"({stats['nb_modifiees']} modif / "
              f"{stats['nb_ajoutees']} ajout / "
              f"{stats['nb_supprimees']} suppr)")

        resultats_globaux.append({
            'test'            : f"#{num}",
            'fichier_entree'  : fichier_test.name,
            'fichier_reponse' : fichier_reponse.name,
            'lignes_entree'   : stats['total_entree'],
            'lignes_sortie'   : stats['total_sortie'],
            'identiques'      : stats['nb_identiques'],
            'modifiees'       : stats['nb_modifiees'],
            'ajoutees'        : stats['nb_ajoutees'],
            'supprimees'      : stats['nb_supprimees'],
            'total_diff'      : stats['nb_diff'],
            'similarite'      : stats['similarite'],
            'differences'     : differences   # ← pour le HTML plus tard
        })

    # Export CSV
    csv_path = DIR_RESULTATS / f"{NOM_RAPPORT}.csv"
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['test','fichier_entree','fichier_reponse',
                      'lignes_entree','lignes_sortie','identiques',
                      'modifiees','ajoutees','supprimees','total_diff','similarite']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in resultats_globaux:
            row = {k: r[k] for k in fieldnames}
            writer.writerow(row)

    # Export JSON (base pour le HTML)
    json_path = DIR_RESULTATS / f"{NOM_RAPPORT}.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(resultats_globaux, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 60)
    print(f"  Rapports TXT : {DIR_RESULTATS}/#diffX_rapport.txt")
    print(f"  CSV          : {csv_path.name}")
    print(f"  JSON         : {json_path.name}  ← base pour le HTML")
    print("=" * 60)


if __name__ == '__main__':
    main()