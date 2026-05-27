#!/usr/bin/env python3
"""
Comparateur COBOL - Ollama Granite Test Series
Compare #Xtest.cbl (questions) vs #resultX.cbl (réponses Ollama)
"""

import os
import csv
import json
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

DIR_RESULTATS.mkdir(parents=True, exist_ok=True)


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
    if IGNORER_CASSE:
        ligne = ligne.lower()
    if IGNORER_ESPACES:
        ligne = ' '.join(ligne.split())
    return ligne


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
        elif normaliser(lignes1[i]) == normaliser(lignes2[i]):
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


def ecrire_rapport_txt(num, stats, differences, date_exec, num_exec, chemin):
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write(f"   RAPPORT DE COMPARAISON - {LANGAGE.upper()} TEST #{num}\n")
        f.write("=" * 60 + "\n")
        f.write(f"  Date d'exécution  : {date_exec}\n")
        f.write(f"  Numéro exécution  : #{num_exec}\n")
        f.write(f"  Langage           : {LANGAGE.upper()}\n")
        f.write(f"  Entrée            : #{num}test{EXTENSION}\n")
        f.write(f"  Réponse Granite   : #result{num}{EXTENSION}\n")
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

        lignes_test    = lire_fichier(fichier_test)
        lignes_reponse = lire_fichier(fichier_reponse)
        stats, differences = comparer(lignes_test, lignes_reponse)

        rapport_txt = DIR_RESULTATS / f"#diff{num}_rapport.txt"
        ecrire_rapport_txt(num, stats, differences, date_exec, num_exec, rapport_txt)

        print(f"    Similarité  : {stats['similarite']}%")
        print(f"    Différences : {stats['nb_diff']} "
              f"({stats['nb_modifiees']} modif / "
              f"{stats['nb_ajoutees']} ajout / "
              f"{stats['nb_supprimees']} suppr)")
        print(f"    Rapport     : {rapport_txt.name}")

        resultats_globaux.append({
            'execution'       : num_exec,
            'date'            : date_exec,
            'langage'         : LANGAGE,
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
            'differences'     : differences
        })

    csv_path   = DIR_RESULTATS / f"{NOM_RAPPORT}.csv"
    csv_fields = [
        'execution', 'date', 'langage', 'test',
        'fichier_entree', 'fichier_reponse',
        'lignes_entree', 'lignes_sortie',
        'identiques', 'modifiees', 'ajoutees',
        'supprimees', 'total_diff', 'similarite'
    ]
    mode_csv = 'a' if csv_path.exists() else 'w'
    with open(csv_path, mode_csv, newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
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