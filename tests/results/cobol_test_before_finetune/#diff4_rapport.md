# Rapport de comparaison — COBOL — Test #4

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #4 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-08-10 |
| Numéro d'exécution | #3 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 10 |
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
| Lignes supprimées | 10 |
| Total différences | 10 |
| **Similarité globale** | **0.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | SUPPRIMEE | `IDENTIFICATION DIVISION.` | `` |
| 2 | SUPPRIMEE | `PROGRAM-ID. TEST4.` | `` |
| 3 | SUPPRIMEE | `DATA DIVISION.` | `` |
| 4 | SUPPRIMEE | `WORKING-STORAGE SECTION.` | `` |
| 5 | SUPPRIMEE | `01 COUNTER PIC 9(2) VALUE 0.` | `` |
| 6 | SUPPRIMEE | `PROCEDURE DIVISION.` | `` |
| 7 | SUPPRIMEE | `PERFORM UNTIL COUNTER > 5` | `` |
| 8 | SUPPRIMEE | `DISPLAY COUNTER` | `` |
| 9 | SUPPRIMEE | `ADD 1 TO COUNTER` | `` |
| 10 | SUPPRIMEE | `STOP RUN.` | `` |

## Code original (input)

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST4.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 COUNTER PIC 9(2) VALUE 0.
       PROCEDURE DIVISION.
           PERFORM UNTIL COUNTER > 5
               DISPLAY COUNTER
               ADD 1 TO COUNTER
           STOP RUN.

```

## Réponse Granite — code extrait (output normalisé)

```cobol

```

