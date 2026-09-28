# Rapport de comparaison — COBOL — Test #7

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #7 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-09-28 |
| Numéro d'exécution | #2 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 29 |
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
| Lignes supprimées | 29 |
| Total différences | 29 |
| **Similarité globale** | **0.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | SUPPRIMEE | `IDENTIFICATION DIVISION.` | `` |
| 2 | SUPPRIMEE | `PROGRAM-ID. CALCUL-SALAIRE.` | `` |
| 3 | SUPPRIMEE | `DATA DIVISION.` | `` |
| 4 | SUPPRIMEE | `WORKING-STORAGE SECTION.` | `` |
| 5 | SUPPRIMEE | `01 NOM-EMPLOYE     PIC X(30).` | `` |
| 6 | SUPPRIMEE | `01 SALAIRE-BRUT    PIC 9(7)V99.` | `` |
| 7 | SUPPRIMEE | `01 PRIME           PIC 9(5)V99.` | `` |
| 8 | SUPPRIMEE | `01 SALAIRE-NET     PIC 9(7)V99.` | `` |
| 9 | SUPPRIMEE | `01 TAUX-CHARGES    PIC 9V99.` | `` |
| 10 | SUPPRIMEE | `01 CHARGES         PIC 9(7)V99.` | `` |
| 11 | SUPPRIMEE | `PROCEDURE DIVISION.` | `` |
| 12 | SUPPRIMEE | `DEBUT.` | `` |
| 13 | SUPPRIMEE | `DISPLAY "Nom de l'employe : "` | `` |
| 14 | SUPPRIMEE | `ACCEPT NOM-EMPLOYE` | `` |
| 15 | SUPPRIMEE | `DISPLAY "Salaire brut : "` | `` |
| 16 | SUPPRIMEE | `ACCEPT SALAIRE-BRUT` | `` |
| 17 | SUPPRIMEE | `DISPLAY "Prime : "` | `` |
| 18 | SUPPRIMEE | `ACCEPT PRIME.` | `` |
| 19 | SUPPRIMEE | `MOVE 0.23 TO TAUX-CHARGES` | `` |
| 20 | SUPPRIMEE | `COMPUTE SALAIRE-NET =` | `` |
| 21 | SUPPRIMEE | `SALAIRE-BRUT + PRIME - CHARGES` | `` |
| 22 | SUPPRIMEE | `COMPUTE CHARGES =` | `` |
| 23 | SUPPRIMEE | `SALAIRE-BRUT * TAUX-CHARGES` | `` |
| 24 | SUPPRIMEE | `DISPLAY "Employe : " NOM-EMPLOYE` | `` |
| 25 | SUPPRIMEE | `DISPLAY "Salaire brut : " SALAIRE-BRUT` | `` |
| 26 | SUPPRIMEE | `DISPLAY "Prime : " PRIME` | `` |
| 27 | SUPPRIMEE | `DISPLAY "Charges : " CHARGES` | `` |
| 28 | SUPPRIMEE | `DISPLAY "Salaire net : " SALAIRE-NET` | `` |
| 29 | SUPPRIMEE | `STOP-RUN.` | `` |

## Code original (input)

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CALCUL-SALAIRE.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01 NOM-EMPLOYE     PIC X(30).
       01 SALAIRE-BRUT    PIC 9(7)V99.
       01 PRIME           PIC 9(5)V99.
       01 SALAIRE-NET     PIC 9(7)V99.
       01 TAUX-CHARGES    PIC 9V99.
       01 CHARGES         PIC 9(7)V99.

       PROCEDURE DIVISION.

       DEBUT.
           DISPLAY "Nom de l'employe : "
           ACCEPT NOM-EMPLOYE

           DISPLAY "Salaire brut : "
           ACCEPT SALAIRE-BRUT

           DISPLAY "Prime : "
           ACCEPT PRIME.

           MOVE 0.23 TO TAUX-CHARGES

           COMPUTE SALAIRE-NET =
               SALAIRE-BRUT + PRIME - CHARGES

           COMPUTE CHARGES =
               SALAIRE-BRUT * TAUX-CHARGES

           DISPLAY "Employe : " NOM-EMPLOYE
           DISPLAY "Salaire brut : " SALAIRE-BRUT
           DISPLAY "Prime : " PRIME
           DISPLAY "Charges : " CHARGES
           DISPLAY "Salaire net : " SALAIRE-NET

           STOP-RUN.
```

## Réponse Granite — code extrait (output normalisé)

```cobol

```

