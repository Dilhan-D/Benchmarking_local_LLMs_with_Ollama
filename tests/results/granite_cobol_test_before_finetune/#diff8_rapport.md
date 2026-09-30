# Rapport de comparaison — COBOL — Test #8

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #8 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-09-30 |
| Numéro d'exécution | #9 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 22 |
| Lignes output (utiles) | 24 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 20 |
| Lignes modifiées | 2 |
| Lignes ajoutées | 2 |
| Lignes supprimées | 0 |
| Total différences | 4 |
| **Similarité globale** | **90.91%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 10 | AJOUTEE | `` | `COPY DDS-ALL-FORMATS OF DSPF-CLIENT INTO DSPF-CLIENT.  -- Inclure les formats du fichier DDS` |
| 12 | MODIFIEE | `COPY DDS-ALL-FORMATS OF DSPF-CLIENT.` | `INCLUDE DDS-ALL-FORMATS.  -- Inclure les formats dans la définition de fichier` |
| 18 | MODIFIEE | `MOVE "DUPONT" TO WS-NOM` | `MOVE "Dupont" TO WS-NOM` |
| 20 | AJOUTEE | `` | `-- Utilisez le format approprié pour écrire sur l'écran` |

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
IDENTIFICATION DIVISION.
       PROGRAM-ID. CLIENT01.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.

       FILE-CONTROL.
           SELECT DSPF-CLIENT
               ASSIGN TO WORKSTATION-GESTION.

       DATA DIVISION.
       FILE SECTION.
       
       COPY DDS-ALL-FORMATS OF DSPF-CLIENT INTO DSPF-CLIENT.  -- Inclure les formats du fichier DDS

       FD DSPF-CLIENT.
       01 CLIENT-SCREEN.
           INCLUDE DDS-ALL-FORMATS.  -- Inclure les formats dans la définition de fichier

       WORKING-STORAGE SECTION.
       01 WS-NOM       PIC X(30).
       01 WS-CHOIX     PIC X.

       PROCEDURE DIVISION.

           OPEN I-O DSPF-CLIENT

           MOVE "Dupont" TO WS-NOM
           MOVE "1" TO WS-CHOIX

           -- Utilisez le format approprié pour écrire sur l'écran
           WRITE CLIENT-SCREEN FORMAT "CLIENT"

           CLOSE DSPF-CLIENT

           STOP RUN.
```

