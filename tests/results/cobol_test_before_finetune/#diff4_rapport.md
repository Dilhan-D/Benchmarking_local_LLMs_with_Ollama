# Rapport de comparaison — COBOL — Test #4

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #4 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-08-13 |
| Numéro d'exécution | #12 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 10 |
| Lignes output (utiles) | 11 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 10 |
| Lignes modifiées | 0 |
| Lignes ajoutées | 1 |
| Lignes supprimées | 0 |
| Total différences | 1 |
| **Similarité globale** | **100.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 10 | AJOUTEE | `` | `END-PERFORM.` |

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
IDENTIFICATION DIVISION.
PROGRAM-ID. TEST4.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 COUNTER PIC 9(2) VALUE 0.   

PROCEDURE DIVISION.
    PERFORM UNTIL COUNTER > 5     
        DISPLAY COUNTER           
        ADD 1 TO COUNTER        
    END-PERFORM.
STOP RUN.
```

