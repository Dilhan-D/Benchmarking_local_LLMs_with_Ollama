# Rapport de comparaison — CLLE — Test #5

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #5 |
| Langage IBM i | CLLE |
| Date d'exécution | 2026-07-10 15:08:54 |
| Numéro d'exécution | #8 |
| Modèle utilisé | granite4.1:8b |
| Lignes input | 7 |
| Lignes output (extrait) | 7 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 1 |
| Lignes modifiées | 6 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 6 |
| **Similarité globale** | **14.29%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | MODIFIEE | `PGM` | `DCL VAR(&PARAM) TYPE(*CHAR) LEN(10) VALUE('TEST')` |
| 2 | MODIFIEE | `    DCL VAR(&PARAM) TYPE(*CHAR) LEN(10) VALUE('TEST')` | `    DCL VAR(&RESULTAT) TYPE(*DEC) LEN(5 0)` |
| 3 | MODIFIEE | `    /* ERREUR 1: bibliothèque non qualifiée */` | `    /* Appel du programme sans erreur */` |
| 4 | MODIFIEE | `    CALL PGM(MONPGM) PARM(&PARAM)` | `    CALL PGM(MYLIB/MONPGM) PARM(&PARAM)` |
| 5 | MODIFIEE | `    /* ERREUR 2: variable non déclarée */` | `    /* Appel du second programme avec une variable déclarée et qualifiée par la bibliothèque */` |
| 6 | MODIFIEE | `    CALL PGM(MYLIB/CALCPGM) PARM(&RESULTAT)` | `    CALL MYLIB/CALCPGM PARM(&RESULTAT)` |

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

