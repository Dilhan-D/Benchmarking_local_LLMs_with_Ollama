# Rapport de comparaison — CLLE — Test #5

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #5 |
| Langage IBM i | CLLE |
| Date d'exécution | 2026-08-13 |
| Numéro d'exécution | #1 |
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
| Lignes identiques | 2 |
| Lignes modifiées | 3 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 1 |
| Total différences | 4 |
| **Similarité globale** | **40.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | SUPPRIMEE | `PGM` | `` |
| 3 | MODIFIEE | `CALL PGM(MONPGM) PARM(&PARAM)` | `DCL VAR(&RESULTAT) TYPE(*DEC) LEN(5 0)` |
| 4 | MODIFIEE | `CALL PGM(MYLIB/CALCPGM) PARM(&RESULTAT)` | `CALL PGM(MYLIB/MONPGM) PARM(&PARAM)` |
| 5 | MODIFIEE | `` | `CALL MYLIB/CALCPGM PARM(&RESULTAT)` |

## Code original (input)

```cl
PGM

    DCL VAR(&PARAM) TYPE(*CHAR) LEN(10) VALUE('TEST')

    /* ERREUR 1: bibliothèque non qualifiée */
    CALL PGM(MONPGM) PARM(&PARAM)

    /* ERREUR 2: variable non déclarée */
    CALL PGM(MYLIB/CALCPGM) PARM(&RESULTAT)

ENDPGM
```

## Réponse Granite — code extrait (output normalisé)

```cl
DCL VAR(&PARAM) TYPE(*CHAR) LEN(10) VALUE('TEST')
    DCL VAR(&RESULTAT) TYPE(*DEC) LEN(5 0)

    /* Appel du programme sans erreur */
    CALL PGM(MYLIB/MONPGM) PARM(&PARAM)

    /* Appel du second programme avec une variable déclarée et qualifiée par la bibliothèque */
    CALL MYLIB/CALCPGM PARM(&RESULTAT)
    
ENDPGM
```

