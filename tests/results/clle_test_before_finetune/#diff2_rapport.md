# Rapport de comparaison — CLLE — Test #2

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #2 |
| Langage IBM i | CLLE |
| Date d'exécution | 2026-07-30 |
| Numéro d'exécution | #1 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 6 |
| Lignes output (utiles) | 7 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 3 |
| Lignes modifiées | 4 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 1 |
| Total différences | 5 |
| **Similarité globale** | **50.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | SUPPRIMEE | `PGM` | `` |
| 3 | MODIFIEE | `DCL VAR(&AGE)  TYPE(*DEC)  LEN(3)  VALUE(25)` | `DCL VAR(&AGE)  TYPE(*DEC)  LEN(3 0) VALUE(25)` |
| 5 | MODIFIEE | `SNDMSG MSG('Bonjour ' *CAT &NOM) TOUSR(*SYSOPR)` | `DCL VAR(&MESSAGE) TYPE(*CHAR) LEN(40)` |
| 6 | MODIFIEE | `` | `CHGVAR VAR(&MESSAGE) VALUE('Bonjour ' *CAT &NOM)` |
| 7 | MODIFIEE | `` | `SNDMSG MSG(&MESSAGE) TOUSR(*SYSOPR)` |

## Code original (input)

```cl
PGM

    DCL VAR(&NOM)  TYPE(*CHAR) LEN(20) VALUE('DUPONT')
    DCL VAR(&AGE)  TYPE(*DEC)  LEN(3)  VALUE(25)
    /* ERREUR 1: LEN(3) sans décimales sur *DEC doit être LEN(3 0) */

    SNDMSG MSG(&NOM) TOUSR(*SYSOPR)

    /* ERREUR 2: on ne peut pas concaténer directement */
    SNDMSG MSG('Bonjour ' *CAT &NOM) TOUSR(*SYSOPR)

ENDPGM
```

## Réponse Granite — code extrait (output normalisé)

```cl
/* Programme (PGM) pour démontrer l'utilisation de variables et envoi de messages */

DCL VAR(&NOM)  TYPE(*CHAR) LEN(20) VALUE('DUPONT')   /* Déclaration d'une variable &NOM de type caractère avec une longueur de 20, initialisée à 'DUPONT' */
DCL VAR(&AGE)  TYPE(*DEC)  LEN(3 0) VALUE(25)       /* Correction ERREUR 1 : ajout de 0 pour spécifier qu'il n'y a pas de décimales */

/* Message envoyé avec le nom initialisé */
SNDMSG MSG(&NOM) TOUSR(*SYSOPR)                     /* Envoie un message contenant la valeur de &NOM à l'utilisateur *SYSOPR */

/* Construction d'un message concaténant une chaîne et la variable &NOM */
DCL VAR(&MESSAGE) TYPE(*CHAR) LEN(40)                /* Déclare une variable pour stocker le message final */
CHGVAR VAR(&MESSAGE) VALUE('Bonjour ' *CAT &NOM)    /* Concatène 'Bonjour ' avec &NOM dans &MESSAGE */

/* Envoie le message concaténé à l'utilisateur système */
SNDMSG MSG(&MESSAGE) TOUSR(*SYSOPR)                  /* Envoie le message final à l'utilisateur *SYSOPR */

ENDPGM                                                /* Termine le programme */
```

