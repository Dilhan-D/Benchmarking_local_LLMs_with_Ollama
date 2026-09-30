# Rapport de comparaison — CLLE — Test #1

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #1 |
| Langage IBM i | CLLE |
| Date d'exécution | 2026-09-30 |
| Numéro d'exécution | #2 |
| Modèle utilisé | granite4.2:8b |
| Lignes input (utiles) | 13 |
| Lignes output (utiles) | 15 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 2 |
| Lignes modifiées | 13 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 13 |
| **Similarité globale** | **15.38%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 2 | MODIFIEE | `DCL VAR(&NOM)     TYPE(*CHAR)   LEN(30) VALUE('GILLES')` | `DCL VAR(&NOM      CHAR(30)) VALUE('GILLES')` |
| 3 | MODIFIEE | `DCL VAR(&AGE)     TYPE(*DEC)    LEN(3 0) VALUE(34)` | `DCL VAR(&AGE      DEC(3 0)) VALUE(34)` |
| 4 | MODIFIEE | `DCL VAR(&SALAIRE) TYPE(*DEC)    LEN(9 2) VALUE(2500.00)` | `DCL VAR(&SALAIRE  DEC(9 2)) VALUE(2500.00)` |
| 5 | MODIFIEE | `DCL VAR(&ACTIF)   TYPE(*LGL)    VALUE('1')` | `DCL VAR(&ACTIF    LOGIC) VALUE('1')` |
| 6 | MODIFIEE | `DCL VAR(&MSGID)   TYPE(*CHAR)   LEN(7)` | `DCL VAR(&MSGID    CHAR(7))` |
| 7 | MODIFIEE | `DCL VAR(&CODE)    TYPE(*INTEGER) LEN(10)` | `DCL VAR(&CODE     *INTEGER LEN(10))` |
| 8 | MODIFIEE | `DCL VAR(&LIBELLE) TYPE(*CHAR)` | `DCL VAR(&LIBELLE  CHAR(30))` |
| 9 | MODIFIEE | `DCL VAR(&MONTANT) TYPE(*DEC)    LEN(9 2) VALUE('ABC')` | `DCL VAR(&MONTANT  DEC(9 2)) VALUE('0.00')` |
| 10 | MODIFIEE | `IF COND(&AGE *GE 18) THEN(DO)` | `IF COND(&AGE *GE 18)` |
| 12 | MODIFIEE | `ENDDO` | `ELSE` |
| 13 | MODIFIEE | `ELSE CMD(SNDMSG MSG('Mineur') TOUSR(*SYSOPR))` | `SNDMSG MSG('Mineur') TOUSR(*SYSOPR)` |
| 14 | MODIFIEE | `` | `ENDIF` |
| 15 | MODIFIEE | `` | `ENDPGM` |

## Code original (input)

```cl
/*********************************************/
/* Programme CL - Commandes de base          */
/* Erreurs volontaires pour test Granite     */
/*********************************************/
PGM

    /* Déclarations de variables */
    DCL VAR(&NOM)     TYPE(*CHAR)   LEN(30) VALUE('GILLES')
    DCL VAR(&AGE)     TYPE(*DEC)    LEN(3 0) VALUE(34)
    DCL VAR(&SALAIRE) TYPE(*DEC)    LEN(9 2) VALUE(2500.00)
    DCL VAR(&ACTIF)   TYPE(*LGL)    VALUE('1')
    DCL VAR(&MSGID)   TYPE(*CHAR)   LEN(7)

    /* ERREUR 1: TYPE invalide */
    DCL VAR(&CODE)    TYPE(*INTEGER) LEN(10)

    /* ERREUR 2: LEN manquant sur *CHAR */
    DCL VAR(&LIBELLE) TYPE(*CHAR)

    /* ERREUR 3: VALUE incompatible avec *DEC */
    DCL VAR(&MONTANT) TYPE(*DEC)    LEN(9 2) VALUE('ABC')

    /* Test IF simple */
    IF COND(&AGE *GE 18) THEN(DO)
        SNDMSG MSG('Personne majeure') TOUSR(*SYSOPR)
    ENDDO

    /* ERREUR 4: ELSE sans IF */
    ELSE CMD(SNDMSG MSG('Mineur') TOUSR(*SYSOPR))

    /* ERREUR 5: ENDPGM manquant */

```

## Réponse Granite — code extrait (output normalisé)

```cl
PGM
    DCL VAR(&NOM      CHAR(30)) VALUE('GILLES')
    DCL VAR(&AGE      DEC(3 0)) VALUE(34)
    DCL VAR(&SALAIRE  DEC(9 2)) VALUE(2500.00)
    DCL VAR(&ACTIF    LOGIC) VALUE('1')
    DCL VAR(&MSGID    CHAR(7))
    DCL VAR(&CODE     *INTEGER LEN(10))   /* unchanged – valid as written */
    DCL VAR(&LIBELLE  CHAR(30))          /* FIXED: explicit length (was implied only) */
    DCL VAR(&MONTANT  DEC(9 2)) VALUE('0.00') /* FIXED: numeric string, e.g., '0.00' not 'ABC' */

    IF COND(&AGE *GE 18)
        SNDMSG MSG('Personne majeure') TOUSR(*SYSOPR)
    ELSE
        SNDMSG MSG('Mineur') TOUSR(*SYSOPR)
    ENDIF                         /* proper IF‑ELSE block; no standalone ELSE CMD */

    ENDPGM                         /* FIXED: missing terminator */
```

