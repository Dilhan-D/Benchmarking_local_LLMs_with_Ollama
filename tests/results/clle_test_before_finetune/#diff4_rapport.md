# Rapport de comparaison — CLLE — Test #4

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #4 |
| Langage IBM i | CLLE |
| Date d'exécution | 2026-07-27 |
| Numéro d'exécution | #10 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 6 |
| Lignes output (utiles) | 6 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 5 |
| Lignes modifiées | 0 |
| Lignes ajoutées | 1 |
| Lignes supprimées | 1 |
| Total différences | 2 |
| **Similarité globale** | **83.33%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | SUPPRIMEE | `PGM` | `` |
| 6 | AJOUTEE | `` | `ENDDO` |

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

