# Rapport de comparaison — COBOL — Test #1

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #1 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-08-10 |
| Numéro d'exécution | #1 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 5 |
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
| Lignes supprimées | 5 |
| Total différences | 5 |
| **Similarité globale** | **0.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | SUPPRIMEE | `IDENTIFICATION DIVISION.` | `` |
| 2 | SUPPRIMEE | `PROGRAM-ID TEST1` | `` |
| 3 | SUPPRIMEE | `PROCEDURE DIVISION.` | `` |
| 4 | SUPPRIMEE | `PRINT "HELLO"` | `` |
| 5 | SUPPRIMEE | `STOP RUN.` | `` |

## Code original (input)

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID TEST1
       PROCEDURE DIVISION.
           PRINT "HELLO"
           STOP RUN.

```

## Réponse Granite — code extrait (output normalisé)

```cobol

```

