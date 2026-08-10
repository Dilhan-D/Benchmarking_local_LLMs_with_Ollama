# Rapport de comparaison — COBOL — Test #3

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #3 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-08-10 |
| Numéro d'exécution | #2 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 6 |
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
| Lignes supprimées | 6 |
| Total différences | 6 |
| **Similarité globale** | **0.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | SUPPRIMEE | `IDENTIFICATION DIVISION.` | `` |
| 2 | SUPPRIMEE | `PROGRAM-ID. TEST3.` | `` |
| 3 | SUPPRIMEE | `PROCEDURE DIVISION.` | `` |
| 4 | SUPPRIMEE | `DISPLAY "TESTING"` | `` |
| 5 | SUPPRIMEE | `IF 1 = 1` | `` |
| 6 | SUPPRIMEE | `DISPLAY "TRUE"` | `` |

## Code original (input)

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST3.
       PROCEDURE DIVISION.
           DISPLAY "TESTING"
           IF 1 = 1
               DISPLAY "TRUE"
```

## Réponse Granite — code extrait (output normalisé)

```cobol

```

