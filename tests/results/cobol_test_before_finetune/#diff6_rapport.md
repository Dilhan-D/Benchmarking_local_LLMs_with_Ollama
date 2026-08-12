# Rapport de comparaison — COBOL — Test #6

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #6 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-08-11 |
| Numéro d'exécution | #10 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 11 |
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
| Lignes supprimées | 11 |
| Total différences | 11 |
| **Similarité globale** | **0.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | SUPPRIMEE | `IDENTIFICATION DIVISION.` | `` |
| 2 | SUPPRIMEE | `PROGRAM-ID. TEST6` | `` |
| 3 | SUPPRIMEE | `DATA DIVISION.` | `` |
| 4 | SUPPRIMEE | `WORKING-STORAGE SECTION.` | `` |
| 5 | SUPPRIMEE | `01 COUNTER PIC 9.` | `` |
| 6 | SUPPRIMEE | `10 VENOM   PIC(x)` | `` |
| 7 | SUPPRIMEE | `PROCEDURE DIVISION.` | `` |
| 8 | SUPPRIMEE | `PERFORM 3 TIMES` | `` |
| 9 | SUPPRIMEE | `PRINT "ERROR"` | `` |
| 10 | SUPPRIMEE | `COMPUTE 1 = 2` | `` |
| 11 | SUPPRIMEE | `STOP RUN` | `` |

## Code original (input)

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST6
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 COUNTER PIC 9.
       10 VENOM   PIC(x)
       PROCEDURE DIVISION.
           PERFORM 3 TIMES
               PRINT "ERROR"
           COMPUTE 1 = 2
           STOP RUN

```

## Réponse Granite — code extrait (output normalisé)

```cobol

```

