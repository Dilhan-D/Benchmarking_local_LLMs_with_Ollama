# Rapport de comparaison — CLLE — Test #3

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #3 |
| Langage IBM i | CLLE |
| Date d'exécution | 2026-07-30 |
| Numéro d'exécution | #1 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 7 |
| Lignes output (utiles) | 6 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 4 |
| Lignes modifiées | 2 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 1 |
| Total différences | 3 |
| **Similarité globale** | **57.14%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | SUPPRIMEE | `PGM` | `` |
| 4 | MODIFIEE | `SNDMSG MSG('Recu') TOUSR(*SYSOPR)` | `SNDMSG MSG('Reçu') TOUSR(*SYSOPR)` |
| 6 | MODIFIEE | `ELSE CMD(SNDMSG MSG('Echoue') TOUSR(*SYSOPR))` | `ELSE CMD(SNDMSG MSG('Échoue') TOUSR(*SYSOPR))` |

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

