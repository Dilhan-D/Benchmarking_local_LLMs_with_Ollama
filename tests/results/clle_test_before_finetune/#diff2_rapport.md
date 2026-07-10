# Rapport de comparaison — CLLE — Test #2

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #2 |
| Langage IBM i | CLLE |
| Date d'exécution | 2026-07-10 15:08:54 |
| Numéro d'exécution | #8 |
| Modèle utilisé | granite4.1:8b |
| Lignes input | 8 |
| Lignes output (extrait) | 11 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 0 |
| Lignes modifiées | 8 |
| Lignes ajoutées | 3 |
| Lignes supprimées | 0 |
| Total différences | 11 |
| **Similarité globale** | **0.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | MODIFIEE | `PGM` | `/* Programme (PGM) pour démontrer l'utilisation de variables et envoi de messages */` |
| 2 | MODIFIEE | `    DCL VAR(&NOM)  TYPE(*CHAR) LEN(20) VALUE('DUPONT')` | `DCL VAR(&NOM)  TYPE(*CHAR) LEN(20) VALUE('DUPONT')   /* Déclaration d'une variable &NOM de type caractère avec une longueur de 20, initialisée à 'DUPONT' */` |
| 3 | MODIFIEE | `    DCL VAR(&AGE)  TYPE(*DEC)  LEN(3)  VALUE(25)` | `DCL VAR(&AGE)  TYPE(*DEC)  LEN(3 0) VALUE(25)       /* Correction ERREUR 1 : ajout de 0 pour spécifier qu'il n'y a pas de décimales */` |
| 4 | MODIFIEE | `    /* ERREUR 1: LEN(3) sans décimales sur *DEC doit être LEN(3 0) */` | `/* Message envoyé avec le nom initialisé */` |
| 5 | MODIFIEE | `    SNDMSG MSG(&NOM) TOUSR(*SYSOPR)` | `SNDMSG MSG(&NOM) TOUSR(*SYSOPR)                     /* Envoie un message contenant la valeur de &NOM à l'utilisateur *SYSOPR */` |
| 6 | MODIFIEE | `    /* ERREUR 2: on ne peut pas concaténer directement */` | `/* Construction d'un message concaténant une chaîne et la variable &NOM */` |
| 7 | MODIFIEE | `    SNDMSG MSG('Bonjour ' *CAT &NOM) TOUSR(*SYSOPR)` | `DCL VAR(&MESSAGE) TYPE(*CHAR) LEN(40)                /* Déclare une variable pour stocker le message final */` |
| 8 | MODIFIEE | `ENDPGM` | `CHGVAR VAR(&MESSAGE) VALUE('Bonjour ' *CAT &NOM)    /* Concatène 'Bonjour ' avec &NOM dans &MESSAGE */` |
| 9 | AJOUTEE | `` | `/* Envoie le message concaténé à l'utilisateur système */` |
| 10 | AJOUTEE | `` | `SNDMSG MSG(&MESSAGE) TOUSR(*SYSOPR)                  /* Envoie le message final à l'utilisateur *SYSOPR */` |
| 11 | AJOUTEE | `` | `ENDPGM                                                /* Termine le programme */` |

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

