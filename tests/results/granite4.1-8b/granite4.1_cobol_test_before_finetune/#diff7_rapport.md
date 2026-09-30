# Rapport de comparaison — COBOL — Test #7

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #7 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-09-30 |
| Numéro d'exécution | #11 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 29 |
| Lignes output (utiles) | 26 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 20 |
| Lignes modifiées | 9 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 9 |
| **Similarité globale** | **68.97%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 9 | MODIFIEE | `01 TAUX-CHARGES    PIC 9V99.` | `01 TAUX-CHARGES    PIC 9V99 VALUE 23.   *> Initialise le taux de charges à 23%` |
| 13 | MODIFIEE | `DISPLAY "Nom de l'employe : "` | `DISPLAY "Nom de l'employé : "` |
| 18 | MODIFIEE | `ACCEPT PRIME.` | `ACCEPT PRIME` |
| 19 | MODIFIEE | `MOVE 0.23 TO TAUX-CHARGES` | `COMPUTE CHARGES = SALAIRE-BRUT * TAUX-CHARGES / 100` |
| 20 | MODIFIEE | `COMPUTE SALAIRE-NET =` | `COMPUTE SALAIRE-NET = SALAIRE-BRUT + PRIME - CHARGES` |
| 21 | MODIFIEE | `SALAIRE-BRUT + PRIME - CHARGES` | `DISPLAY "Employé : " NOM-EMPLOYE` |
| 22 | MODIFIEE | `COMPUTE CHARGES =` | `` |
| 23 | MODIFIEE | `SALAIRE-BRUT * TAUX-CHARGES` | `` |
| 24 | MODIFIEE | `DISPLAY "Employe : " NOM-EMPLOYE` | `` |

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
IDENTIFICATION DIVISION.
       PROGRAM-ID. CALCUL-SALAIRE.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01 NOM-EMPLOYE     PIC X(30).
       01 SALAIRE-BRUT    PIC 9(7)V99.
       01 PRIME           PIC 9(5)V99.
       01 SALAIRE-NET     PIC 9(7)V99.
       01 TAUX-CHARGES    PIC 9V99 VALUE 23.   *> Initialise le taux de charges à 23%
       01 CHARGES         PIC 9(7)V99.

       PROCEDURE DIVISION.

       DEBUT.
           DISPLAY "Nom de l'employé : "
           ACCEPT NOM-EMPLOYE

           DISPLAY "Salaire brut : "
           ACCEPT SALAIRE-BRUT

           DISPLAY "Prime : "
           ACCEPT PRIME

           *> Calcul des charges
           COMPUTE CHARGES = SALAIRE-BRUT * TAUX-CHARGES / 100

           *> Calcul du salaire net
           COMPUTE SALAIRE-NET = SALAIRE-BRUT + PRIME - CHARGES

           DISPLAY "Employé : " NOM-EMPLOYE
           DISPLAY "Salaire brut : " SALAIRE-BRUT
           DISPLAY "Prime : " PRIME
           DISPLAY "Charges : " CHARGES
           DISPLAY "Salaire net : " SALAIRE-NET

           STOP-RUN.
```

