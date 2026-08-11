# Rapport de comparaison — COBOL — Test #4

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #4 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-08-11 |
| Numéro d'exécution | #9 |
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
| Lignes identiques | 5 |
| Lignes modifiées | 6 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 6 |
| **Similarité globale** | **50.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 5 | MODIFIEE | `01 COUNTER PIC 9(2) VALUE 0.` | `01 COUNTER PIC 9(2) VALUE 0.   *> Déclare un compteur de 2 chiffres, initialisé à 0` |
| 7 | MODIFIEE | `PERFORM UNTIL COUNTER > 5` | `PERFORM UNTIL COUNTER > 5      *> Boucle jusqu'à ce que le compteur soit supérieur à 5` |
| 8 | MODIFIEE | `DISPLAY COUNTER` | `DISPLAY COUNTER            *> Affiche la valeur actuelle du compteur` |
| 9 | MODIFIEE | `ADD 1 TO COUNTER` | `ADD 1 TO COUNTER           *> Incrément le compteur de 1` |
| 10 | MODIFIEE | `STOP RUN.` | `END-PERFORM.` |
| 11 | MODIFIEE | `` | `STOP RUN.                         *> Termine l'exécution du programme` |

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
01 COUNTER PIC 9(2) VALUE 0.   *> Déclare un compteur de 2 chiffres, initialisé à 0

PROCEDURE DIVISION.
    PERFORM UNTIL COUNTER > 5      *> Boucle jusqu'à ce que le compteur soit supérieur à 5
        DISPLAY COUNTER            *> Affiche la valeur actuelle du compteur
        ADD 1 TO COUNTER           *> Incrément le compteur de 1
    END-PERFORM.
STOP RUN.                         *> Termine l'exécution du programme
```

