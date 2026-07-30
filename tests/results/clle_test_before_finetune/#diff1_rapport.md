# Rapport de comparaison — CLLE — Test #1

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #1 |
| Langage IBM i | CLLE |
| Date d'exécution | 2026-07-30 |
| Numéro d'exécution | #1 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 13 |
| Lignes output (utiles) | 17 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 7 |
| Lignes modifiées | 10 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 10 |
| **Similarité globale** | **53.85%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 2 | MODIFIEE | `DCL VAR(&NOM)     TYPE(*CHAR)   LEN(30) VALUE('GILLES')` | `DCL VAR(&NOM)     TYPE(*CHAR)   LEN(30) VALUE('DUPONT')` |
| 3 | MODIFIEE | `DCL VAR(&AGE)     TYPE(*DEC)    LEN(3 0) VALUE(33)` | `DCL VAR(&AGE)     TYPE(*DEC)    LEN(3 0) VALUE(25)` |
| 9 | MODIFIEE | `DCL VAR(&MONTANT) TYPE(*DEC)    LEN(9 2) VALUE('ABC')` | `DCL VAR(&MONTANT) TYPE(*DEC)    LEN(9 2) VALUE(1000.00)` |
| 10 | MODIFIEE | `IF COND(&AGE *GE 18) THEN(DO)` | `IF COND(&AGE *GE 18) THEN(` |
| 12 | MODIFIEE | `ENDDO` | `)` |
| 13 | MODIFIEE | `ELSE CMD(SNDMSG MSG('Mineur') TOUSR(*SYSOPR))` | `ELSE CMD(` |
| 14 | MODIFIEE | `` | `SNDMSG MSG('Mineur') TOUSR(*SYSOPR)` |
| 15 | MODIFIEE | `` | `)` |
| 16 | MODIFIEE | `` | `DSPFF D(Fichier: *ALL) OUTPUT(*OUTFILE) OUTFILE(MONFICHIER) MONMONTANT(&MONTANT)` |
| 17 | MODIFIEE | `` | `ENDPGM;` |

## Code original (input)

```cl
/*********************************************/
/* Programme CL - Commandes de base          */
/* Erreurs volontaires pour test Granite     */
/*********************************************/
PGM

    /* Déclarations de variables */
    DCL VAR(&NOM)     TYPE(*CHAR)   LEN(30) VALUE('GILLES')
    DCL VAR(&AGE)     TYPE(*DEC)    LEN(3 0) VALUE(33)
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
/*********************************************/
/* Programme CL - Commandes de base          */
/* Erreurs volontaires pour test Granite     */
/*********************************************/
PGM

// Déclaration des variables
DCL VAR(&NOM)     TYPE(*CHAR)   LEN(30) VALUE('DUPONT')
DCL VAR(&AGE)     TYPE(*DEC)    LEN(3 0) VALUE(25)
DCL VAR(&SALAIRE) TYPE(*DEC)    LEN(9 2) VALUE(2500.00)
DCL VAR(&ACTIF)   TYPE(*LGL)    VALUE('1')
DCL VAR(&MSGID)   TYPE(*CHAR)   LEN(7)

// Variable pour le code retourné par la condition
DCL VAR(&CODE)    TYPE(*INTEGER) LEN(10)

// Libellé de message à afficher
DCL VAR(&LIBELLE) TYPE(*CHAR)

// Montant numérique (correction nécessaire car 'ABC' n'est pas un nombre)
DCL VAR(&MONTANT) TYPE(*DEC)    LEN(9 2) VALUE(1000.00) // Exemple de valeur numérique

/* 
   Condition pour vérifier l'âge.
   Si &AGE est supérieur ou égal à 18, envoi un message indiquant que la personne est majeure.
   Sinon, envoie un message indiquant que la personne est mineure.
*/
IF COND(&AGE *GE 18) THEN(
    SNDMSG MSG('Personne majeure') TOUSR(*SYSOPR)
)
ELSE CMD(
    SNDMSG MSG('Mineur') TOUSR(*SYSOPR)
)

// Exemple d'utilisation de &MONTANT après correction
DSPFF D(Fichier: *ALL) OUTPUT(*OUTFILE) OUTFILE(MONFICHIER) MONMONTANT(&MONTANT)

*INLR = *ON;  // Indique la fin du programme

ENDPGM;
```

