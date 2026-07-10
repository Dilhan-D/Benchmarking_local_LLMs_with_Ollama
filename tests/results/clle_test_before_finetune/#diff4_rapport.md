# Rapport de comparaison — CLLE — Test #4

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #4 |
| Langage IBM i | CLLE |
| Date d'exécution | 2026-07-10 15:08:54 |
| Numéro d'exécution | #8 |
| Modèle utilisé | granite4.1:8b |
| Lignes input | 7 |
| Lignes output (extrait) | 6 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 0 |
| Lignes modifiées | 6 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 1 |
| Total différences | 7 |
| **Similarité globale** | **0.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | MODIFIEE | `PGM` | `DCL VAR(&I) TYPE(*DEC) LEN(3 0) VALUE(1)` |
| 2 | MODIFIEE | `    DCL VAR(&I) TYPE(*DEC) LEN(3 0) VALUE(1)` | `    DOWHILE COND(&I *LE 5)` |
| 3 | MODIFIEE | `    DOWHILE COND(&I *LE 5)` | `        SNDMSG MSG('Tour de boucle') TOUSR(*SYSOPR)` |
| 4 | MODIFIEE | `        SNDMSG MSG('Tour de boucle') TOUSR(*SYSOPR)` | `        CHGVAR VAR(&I) VALUE(&I + 1)` |
| 5 | MODIFIEE | `        CHGVAR VAR(&I) VALUE(&I + 1)` | `    ENDDO` |
| 6 | MODIFIEE | `    /* ERREUR 1: ENDDO manquant */` | `ENDPGM` |
| 7 | SUPPRIMEE | `ENDPGM` | `` |

## Code original (input)

```cl
PGM

    DCL VAR(&I) TYPE(*DEC) LEN(3 0) VALUE(1)

    DOWHILE COND(&I *LE 5)
        SNDMSG MSG('Tour de boucle') TOUSR(*SYSOPR)
        CHGVAR VAR(&I) VALUE(&I + 1)
    /* ERREUR 1: ENDDO manquant */

ENDPGM
```

## Réponse Granite — code extrait (output normalisé)

```cl
DCL VAR(&I) TYPE(*DEC) LEN(3 0) VALUE(1)

    DOWHILE COND(&I *LE 5)
        SNDMSG MSG('Tour de boucle') TOUSR(*SYSOPR)
        CHGVAR VAR(&I) VALUE(&I + 1)
    ENDDO

ENDPGM
```

