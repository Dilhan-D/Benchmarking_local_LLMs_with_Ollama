# Rapport de comparaison — CLLE — Test #1

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #1 |
| Langage IBM i | CLLE |
| Date d'exécution | 2026-07-10 15:08:54 |
| Numéro d'exécution | #8 |
| Modèle utilisé | granite4.1:8b |
| Lignes input | 24 |
| Lignes output (extrait) | 32 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 12 |
| Lignes modifiées | 12 |
| Lignes ajoutées | 8 |
| Lignes supprimées | 0 |
| Total différences | 20 |
| **Similarité globale** | **37.5%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 6 | MODIFIEE | `    /* Déclarations de variables */` | `// Déclaration des variables` |
| 12 | MODIFIEE | `    /* ERREUR 1: TYPE invalide */` | `// Variable pour le code retourné par la condition` |
| 14 | MODIFIEE | `    /* ERREUR 2: LEN manquant sur *CHAR */` | `// Libellé de message à afficher` |
| 16 | MODIFIEE | `    /* ERREUR 3: VALUE incompatible avec *DEC */` | `// Montant numérique (correction nécessaire car 'ABC' n'est pas un nombre)` |
| 17 | MODIFIEE | `    DCL VAR(&MONTANT) TYPE(*DEC)    LEN(9 2) VALUE('ABC')` | `DCL VAR(&MONTANT) TYPE(*DEC)    LEN(9 2) VALUE(1000.00) // Exemple de valeur numérique` |
| 18 | MODIFIEE | `    /* Test IF simple */` | `/* ` |
| 19 | MODIFIEE | `    IF COND(&AGE *GE 18) THEN(DO)` | `   Condition pour vérifier l'âge.` |
| 20 | MODIFIEE | `        SNDMSG MSG('Personne majeure') TOUSR(*SYSOPR)` | `   Si &AGE est supérieur ou égal à 18, envoi un message indiquant que la personne est majeure.` |
| 21 | MODIFIEE | `    ENDDO` | `   Sinon, envoie un message indiquant que la personne est mineure.` |
| 22 | MODIFIEE | `    /* ERREUR 4: ELSE sans IF */` | `*/` |
| 23 | MODIFIEE | `    ELSE CMD(SNDMSG MSG('Mineur') TOUSR(*SYSOPR))` | `IF COND(&AGE *GE 18) THEN(` |
| 24 | MODIFIEE | `    /* ERREUR 5: ENDPGM manquant */` | `    SNDMSG MSG('Personne majeure') TOUSR(*SYSOPR)` |
| 25 | AJOUTEE | `` | `)` |
| 26 | AJOUTEE | `` | `ELSE CMD(` |
| 27 | AJOUTEE | `` | `    SNDMSG MSG('Mineur') TOUSR(*SYSOPR)` |
| 28 | AJOUTEE | `` | `)` |
| 29 | AJOUTEE | `` | `// Exemple d'utilisation de &MONTANT après correction` |
| 30 | AJOUTEE | `` | `DSPFF D(Fichier: *ALL) OUTPUT(*OUTFILE) OUTFILE(MONFICHIER) MONMONTANT(&MONTANT)` |
| 31 | AJOUTEE | `` | `*INLR = *ON;  // Indique la fin du programme` |
| 32 | AJOUTEE | `` | `ENDPGM;` |

## Code original (input)

```cl
/*********************************************/
/* Programme CL - Commandes de base          */
/* Erreurs volontaires pour test Granite     */
/*********************************************/
PGM

    /* Déclarations de variables */
    DCL VAR(&NOM)     TYPE(*CHAR)   LEN(30) VALUE('DUPONT')
    DCL VAR(&AGE)     TYPE(*DEC)    LEN(3 0) VALUE(25)
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

