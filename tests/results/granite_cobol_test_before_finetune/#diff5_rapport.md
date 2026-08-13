# Rapport de comparaison — COBOL — Test #5

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #5 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-08-13 |
| Numéro d'exécution | #1 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 8 |
| Lignes output (utiles) | 9 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 5 |
| Lignes modifiées | 4 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 4 |
| **Similarité globale** | **62.5%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 4 | MODIFIEE | `01 VAL1 PIC 9(3).` | `WORKING-STORAGE SECTION.` |
| 5 | MODIFIEE | `` | `01 VAL1 PIC X(3).` |
| 6 | MODIFIEE | `MOVE "ABC" TO VAL1.` | `MOVE "ABC" TO VAL1` |
| 7 | MODIFIEE | `DISPLAY VAL1.` | `DISPLAY VAL1` |

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
IDENTIFICATION DIVISION.
PROGRAM-ID. TEST5.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 VAL1 PIC X(3).  

PROCEDURE DIVISION.
    MOVE "ABC" TO VAL1  
    DISPLAY VAL1        
    STOP RUN.
```

