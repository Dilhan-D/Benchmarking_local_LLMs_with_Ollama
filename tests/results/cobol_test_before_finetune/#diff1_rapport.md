# Rapport de comparaison — COBOL — Test #1

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #1 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-08-11 |
| Numéro d'exécution | #6 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 5 |
| Lignes output (utiles) | 5 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 3 |
| Lignes modifiées | 2 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 2 |
| **Similarité globale** | **60.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 2 | MODIFIEE | `PROGRAM-ID TEST1` | `PROGRAM-ID. TEST1.` |
| 4 | MODIFIEE | `PRINT "HELLO"` | `DISPLAY "HELLO".` |

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
IDENTIFICATION DIVISION.
        PROGRAM-ID. TEST1.

        PROCEDURE DIVISION.
            DISPLAY "HELLO".
            STOP RUN.
```

