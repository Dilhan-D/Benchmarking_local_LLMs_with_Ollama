# Rapport de comparaison — CLLE — Test #3

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #3 |
| Langage IBM i | CLLE |
| Date d'exécution | 2026-07-10 15:08:54 |
| Numéro d'exécution | #8 |
| Modèle utilisé | granite4.1:8b |
| Lignes input | 8 |
| Lignes output (extrait) | 10 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 0 |
| Lignes modifiées | 8 |
| Lignes ajoutées | 2 |
| Lignes supprimées | 0 |
| Total différences | 10 |
| **Similarité globale** | **0.0%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | MODIFIEE | `PGM` | `/* Programme (PGM) pour vérifier un score et envoyer un message en conséquence */` |
| 2 | MODIFIEE | `    DCL VAR(&SCORE) TYPE(*DEC) LEN(3 0) VALUE(75)` | `DCL VAR(&SCORE) TYPE(*DEC) LEN(3 0) VALUE(75)   /* Déclaration d'une variable &SCORE de type décimal avec une longueur de 3 chiffres et 0 décimale, initialisée à la valeur 75 */` |
| 3 | MODIFIEE | `    IF COND(&SCORE >= 50) THEN(DO)` | `/* Conditionnelle pour vérifier si le score est supérieur ou égal à 50 */` |
| 4 | MODIFIEE | `    /* ERREUR 1: >= invalide en CL, doit être *GE */` | `IF COND(&SCORE >= 50) THEN(DO)                 /* Si &SCORE est ≥ 50, exécute les instructions suivantes : */` |
| 5 | MODIFIEE | `        SNDMSG MSG('Recu') TOUSR(*SYSOPR)` | `    SNDMSG MSG('Reçu') TOUSR(*SYSOPR)        /* Envoie un message 'Reçu' à l'utilisateur *SYSOPR */` |
| 6 | MODIFIEE | `    ENDDO` | `ENDDO                                        /* Fin du bloc DO */` |
| 7 | MODIFIEE | `    ELSE CMD(SNDMSG MSG('Echoue') TOUSR(*SYSOPR))` | `/* Instruction ELSE pour gérer le cas où la condition initiale est fausse (c'est-à-dire &SCORE < 50) */` |
| 8 | MODIFIEE | `ENDPGM` | `ELSE CMD(SNDMSG MSG('Échoue') TOUSR(*SYSOPR)) /* Si &SCORE est inférieur à 50, envoie un message 'Échoue' à l'utilisateur *SYSOPR */` |
| 9 | AJOUTEE | `` | `/* Fin du programme (ENDPGM) */` |
| 10 | AJOUTEE | `` | `ENDPGM` |

## Code original (input)

```cl
PGM

    DCL VAR(&SCORE) TYPE(*DEC) LEN(3 0) VALUE(75)

    IF COND(&SCORE >= 50) THEN(DO)
    /* ERREUR 1: >= invalide en CL, doit être *GE */
        SNDMSG MSG('Recu') TOUSR(*SYSOPR)
    ENDDO
    ELSE CMD(SNDMSG MSG('Echoue') TOUSR(*SYSOPR))

ENDPGM
```

## Réponse Granite — code extrait (output normalisé)

```cl
/* Programme (PGM) pour vérifier un score et envoyer un message en conséquence */
 
DCL VAR(&SCORE) TYPE(*DEC) LEN(3 0) VALUE(75)   /* Déclaration d'une variable &SCORE de type décimal avec une longueur de 3 chiffres et 0 décimale, initialisée à la valeur 75 */

/* Conditionnelle pour vérifier si le score est supérieur ou égal à 50 */
IF COND(&SCORE >= 50) THEN(DO)                 /* Si &SCORE est ≥ 50, exécute les instructions suivantes : */
    
    SNDMSG MSG('Reçu') TOUSR(*SYSOPR)        /* Envoie un message 'Reçu' à l'utilisateur *SYSOPR */

ENDDO                                        /* Fin du bloc DO */

/* Instruction ELSE pour gérer le cas où la condition initiale est fausse (c'est-à-dire &SCORE < 50) */
ELSE CMD(SNDMSG MSG('Échoue') TOUSR(*SYSOPR)) /* Si &SCORE est inférieur à 50, envoie un message 'Échoue' à l'utilisateur *SYSOPR */

/* Fin du programme (ENDPGM) */
ENDPGM
```

