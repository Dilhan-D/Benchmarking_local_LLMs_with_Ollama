# Rapport de comparaison — COBOL — Test #5

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #5 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-08-10 |
| Numéro d'exécution | #5 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 8 |
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
| Lignes supprimées | 8 |
| Total différences | 8 |
| **Similarité globale** | **0.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | SUPPRIMEE | `IDENTIFICATION DIVISION.` | `` |
| 2 | SUPPRIMEE | `PROGRAM-ID. TEST5.` | `` |
| 3 | SUPPRIMEE | `DATA DIVISION.` | `` |
| 4 | SUPPRIMEE | `01 VAL1 PIC 9(3).` | `` |
| 5 | SUPPRIMEE | `PROCEDURE DIVISION.` | `` |
| 6 | SUPPRIMEE | `MOVE "ABC" TO VAL1.` | `` |
| 7 | SUPPRIMEE | `DISPLAY VAL1.` | `` |
| 8 | SUPPRIMEE | `STOP RUN.` | `` |

## Code original (input)

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST5.
       DATA DIVISION.
       01 VAL1 PIC 9(3).
       PROCEDURE DIVISION.
           MOVE "ABC" TO VAL1.
           DISPLAY VAL1.
           STOP RUN.

```

## Réponse Granite — code extrait (output normalisé)

```cobol

```

