# Rapport de comparaison — COBOL — Test #2

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #2 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-08-10 |
| Numéro d'exécution | #3 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 9 |
| Lignes output (utiles) | 0 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 0 |
| Lignes modifiées | 0 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 9 |
| Total différences | 9 |
| **Similarité globale** | **0.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | SUPPRIMEE | `IDENTIFICATION DIVISION.` | `` |
| 2 | SUPPRIMEE | `PROGRAM-ID. TEST2.` | `` |
| 3 | SUPPRIMEE | `DATA DIVISION.` | `` |
| 4 | SUPPRIMEE | `WORKING-STORAGE SECTION.` | `` |
| 5 | SUPPRIMEE | `01 NAME PIC X(10).` | `` |
| 6 | SUPPRIMEE | `PROCEDURE DIVISION.` | `` |
| 7 | SUPPRIMEE | `MOVE "JOHN" TO NAMES.` | `` |
| 8 | SUPPRIMEE | `DISPLAY NAME.` | `` |
| 9 | SUPPRIMEE | `STOP RUN.` | `` |

## Code original (input)

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST2.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 NAME PIC X(10).
       PROCEDURE DIVISION.
           MOVE "JOHN" TO NAMES.
           DISPLAY NAME.
           STOP RUN.

```

## Réponse Granite — code extrait (output normalisé)

```cobol

```

