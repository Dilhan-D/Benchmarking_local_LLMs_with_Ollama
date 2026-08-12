# Rapport de comparaison — COBOL — Test #2

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #2 |
| Langage IBM i | COBOL |
| Date d'exécution | 2026-08-12 |
| Numéro d'exécution | #11 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 9 |
| Lignes output (utiles) | 9 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 8 |
| Lignes modifiées | 1 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 1 |
| **Similarité globale** | **88.89%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 7 | MODIFIEE | `MOVE "JOHN" TO NAMES.` | `MOVE "JOHN" TO NAME.` |

## Code original (input)

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST2.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 NAME PIC X(10).
       PROCEDURE DIVISION.
           MOVE "JOHN" TO NAMES.
           DISPLAY NAME.
           STOP RUN.

```

## Réponse Granite — code extrait (output normalisé)

```cobol
IDENTIFICATION DIVISION.
        PROGRAM-ID. TEST2.

        DATA DIVISION.
        WORKING-STORAGE SECTION.
        01 NAME PIC X(10).

        PROCEDURE DIVISION.
            MOVE "JOHN" TO NAME.
            DISPLAY NAME.
            STOP RUN.
```

