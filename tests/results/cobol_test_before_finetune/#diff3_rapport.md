# Rapport de comparaison — COBOL — Test #3

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #3 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-08-11 |
| Numéro d'exécution | #9 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 6 |
| Lignes output (utiles) | 8 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 4 |
| Lignes modifiées | 4 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 4 |
| **Similarité globale** | **66.67%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 4 | MODIFIEE | `DISPLAY "TESTING"` | `DISPLAY "TESTING".` |
| 6 | MODIFIEE | `DISPLAY "TRUE"` | `DISPLAY "TRUE".` |
| 7 | MODIFIEE | `` | `END-IF.` |
| 8 | MODIFIEE | `` | `STOP RUN.` |

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
IDENTIFICATION DIVISION.
        PROGRAM-ID. TEST3.
        PROCEDURE DIVISION.
            DISPLAY "TESTING".
            IF 1 = 1
                DISPLAY "TRUE".
            END-IF.
        STOP RUN.
```

