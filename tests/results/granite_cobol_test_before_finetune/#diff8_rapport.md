# Rapport de comparaison — COBOL — Test #8

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #8 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-09-30 |
| Numéro d'exécution | #6 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 22 |
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
| Lignes supprimées | 22 |
| Total différences | 22 |
| **Similarité globale** | **0.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | SUPPRIMEE | `IDENTIFICATION DIVISION.` | `` |
| 2 | SUPPRIMEE | `PROGRAM-ID. CLIENT01.` | `` |
| 3 | SUPPRIMEE | `ENVIRONMENT DIVISION.` | `` |
| 4 | SUPPRIMEE | `INPUT-OUTPUT SECTION.` | `` |
| 5 | SUPPRIMEE | `FILE-CONTROL.` | `` |
| 6 | SUPPRIMEE | `SELECT DSPF-CLIENT` | `` |
| 7 | SUPPRIMEE | `ASSIGN TO WORKSTATION-GESTION.` | `` |
| 8 | SUPPRIMEE | `DATA DIVISION.` | `` |
| 9 | SUPPRIMEE | `FILE SECTION.` | `` |
| 10 | SUPPRIMEE | `FD DSPF-CLIENT.` | `` |
| 11 | SUPPRIMEE | `01 CLIENT-SCREEN.` | `` |
| 12 | SUPPRIMEE | `COPY DDS-ALL-FORMATS OF DSPF-CLIENT.` | `` |
| 13 | SUPPRIMEE | `WORKING-STORAGE SECTION.` | `` |
| 14 | SUPPRIMEE | `01 WS-NOM       PIC X(30).` | `` |
| 15 | SUPPRIMEE | `01 WS-CHOIX     PIC X.` | `` |
| 16 | SUPPRIMEE | `PROCEDURE DIVISION.` | `` |
| 17 | SUPPRIMEE | `OPEN I-O DSPF-CLIENT` | `` |
| 18 | SUPPRIMEE | `MOVE "DUPONT" TO WS-NOM` | `` |
| 19 | SUPPRIMEE | `MOVE "1" TO WS-CHOIX` | `` |
| 20 | SUPPRIMEE | `WRITE CLIENT-SCREEN FORMAT "CLIENT"` | `` |
| 21 | SUPPRIMEE | `CLOSE DSPF-CLIENT` | `` |
| 22 | SUPPRIMEE | `STOP RUN.` | `` |

## Code original (input)

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CLIENT01.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.

       FILE-CONTROL.
           SELECT DSPF-CLIENT
               ASSIGN TO WORKSTATION-GESTION.

       DATA DIVISION.
       FILE SECTION.

       FD DSPF-CLIENT.
       01 CLIENT-SCREEN.
           COPY DDS-ALL-FORMATS OF DSPF-CLIENT.

       WORKING-STORAGE SECTION.
       01 WS-NOM       PIC X(30).
       01 WS-CHOIX     PIC X.

       PROCEDURE DIVISION.

           OPEN I-O DSPF-CLIENT

           MOVE "DUPONT" TO WS-NOM
           MOVE "1" TO WS-CHOIX

           WRITE CLIENT-SCREEN FORMAT "CLIENT"

           CLOSE DSPF-CLIENT

           STOP RUN.
```

## Réponse Granite — code extrait (output normalisé)

```cobol

```

