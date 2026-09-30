# Rapport de comparaison — COBOL — Test #9

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #9 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-09-30 |
| Numéro d'exécution | #11 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 15 |
| Lignes output (utiles) | 15 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 10 |
| Lignes modifiées | 5 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 5 |
| **Similarité globale** | **66.67%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 5 | MODIFIEE | `01  WS-PRIX       PIC 9(5)V99.` | `01 WS-PRIX       PIC 9(5)V99.` |
| 6 | MODIFIEE | `01  WS-QUANTITE   PIC 9(3).` | `01 WS-QUANTITE   PIC 9(3).` |
| 7 | MODIFIEE | `01  WS-TOTAL      PIC 9(7)V99.` | `01 WS-TOTAL      PIC 9(7)V99.` |
| 11 | MODIFIEE | `DISPLAY "Entrez la quantite : "` | `DISPLAY "Entrez la quantité : "` |
| 13 | MODIFIEE | `COMPUTE WS-TOTAL = WS-PRIX + WS-QUANTITE` | `COMPUTE WS-TOTAL = WS-PRIX * WS-QUANTITE` |

## Code original (input)

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CALCUL-PRIX.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01  WS-PRIX       PIC 9(5)V99.
       01  WS-QUANTITE   PIC 9(3).
       01  WS-TOTAL      PIC 9(7)V99.

       PROCEDURE DIVISION.

           DISPLAY "Entrez le prix : "
           ACCEPT WS-PRIX

           DISPLAY "Entrez la quantite : "
           ACCEPT WS-QUANTITE

           COMPUTE WS-TOTAL = WS-PRIX + WS-QUANTITE

           DISPLAY "Prix total : " WS-TOTAL

           STOP-RUN.
```

## Réponse Granite — code extrait (output normalisé)

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. CALCUL-PRIX.

DATA DIVISION.
WORKING-STORAGE SECTION.

01 WS-PRIX       PIC 9(5)V99.
01 WS-QUANTITE   PIC 9(3).
01 WS-TOTAL      PIC 9(7)V99.

PROCEDURE DIVISION.

    DISPLAY "Entrez le prix : "
    ACCEPT WS-PRIX

    DISPLAY "Entrez la quantité : "
    ACCEPT WS-QUANTITE

    COMPUTE WS-TOTAL = WS-PRIX * WS-QUANTITE

    DISPLAY "Prix total : " WS-TOTAL

    STOP-RUN.
```

