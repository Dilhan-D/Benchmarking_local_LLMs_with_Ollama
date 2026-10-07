# Rapport de comparaison — CLLE — Test #2

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #2 |
| Langage IBM i | CLLE |
| Date d'exécution | 2026-10-07 |
| Numéro d'exécution | #3 |
| Modèle utilisé | granite4.2:8b |
| Lignes input (utiles) | 17 |
| Lignes output (utiles) | 18 |
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
| Lignes ajoutées | 1 |
| Lignes supprimées | 1 |
| Total différences | 12 |
| **Similarité globale** | **41.18%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 2 | MODIFIEE | `DCL        VAR(&LIB) TYPE(*CHAR) LEN(10)` | `DCL        VAR(&LIB)   TYPE(*CHAR) LEN(10)` |
| 3 | MODIFIEE | `DCL        VAR(&USER) TYPE(*CHAR) LEN(10)` | `DCL        VAR(&USER)  TYPE(*CHAR) LEN(10)` |
| 4 | MODIFIEE | `DCL        VAR(&MODE) TYPE(*CHAR) LEN(10)` | `DCL        VAR(&MODE)  TYPE(*CHAR) LEN(10)` |
| 5 | MODIFIEE | `CHGVAR     VAR(&MESSAGE) +` | `DCL        VAR(&MESSAGE) TYPE(*CHAR) LEN(50)` |
| 6 | MODIFIEE | `VALUE('Debut du traitement')` | `DCL        VAR(&RESULT) TYPE(*CHAR) LEN(10)` |
| 7 | MODIFIEE | `IF         COND(&MODE = '*TEST') THEN` | `CHGVAR     VAR(&MESSAGE) VALUE('Debut du traitement')` |
| 8 | MODIFIEE | `` | `IF         COND(&MODE *EQ '*TEST') THEN` |
| 10 | SUPPRIMEE | `STARTJOB   JOB(&USER)` | `` |
| 12 | MODIFIEE | `PARM(&LIB &USER &PARAM)` | `PARM(&LIB &USER &MODE)` |
| 13 | MODIFIEE | `DLYJOB     TIME(10)` | `DLYJOB     TIME('00:00:10')` |
| 15 | MODIFIEE | `IF         COND(&RESULT *EQ 'OK') THEN(DO)` | `IF         COND(&RESULT *EQ 'OK') THEN` |
| 17 | AJOUTEE | `` | `ENDIF` |

## Code original (input)

```cl
             PGM        PARM(&LIB &USER &MODE)

             DCL        VAR(&LIB) TYPE(*CHAR) LEN(10)
             DCL        VAR(&USER) TYPE(*CHAR) LEN(10)
             DCL        VAR(&MODE) TYPE(*CHAR) LEN(10)

             /* ERREUR : variable non déclarée */
             CHGVAR     VAR(&MESSAGE) +
                        VALUE('Debut du traitement')

             /* ERREUR : syntaxe volontairement incorrecte */
             IF         COND(&MODE = '*TEST') THEN
                SNDPGMMSG MSG('Mode test')
             ENDIF

             /* ERREUR : commande fictive */
             STARTJOB   JOB(&USER)

             /* ERREUR : paramètre inexistant */
             CALL       PGM(MYLIB/MYPGM) +
                        PARM(&LIB &USER &PARAM)

             /* ERREUR : commande avec mauvaise syntaxe */
             DLYJOB     TIME(10)

             /* ERREUR : variable non déclarée */
             CHGVAR     VAR(&RESULT) VALUE('OK')

             /* ERREUR : END manquant / structure incohérente */
             IF         COND(&RESULT *EQ 'OK') THEN(DO)
                SNDPGMMSG MSG('Traitement terminé')

             ENDPGM
```

## Réponse Granite — code extrait (output normalisé)

```cl
PGM        PARM(&LIB &USER &MODE)

  /* Déclarations obligatoires pour toutes les variables utilisées */
  DCL        VAR(&LIB)   TYPE(*CHAR) LEN(10)
  DCL        VAR(&USER)  TYPE(*CHAR) LEN(10)
  DCL        VAR(&MODE)  TYPE(*CHAR) LEN(10)
  DCL        VAR(&MESSAGE) TYPE(*CHAR) LEN(50)  /* Longueur suffisante pour les messages */
  DCL        VAR(&RESULT) TYPE(*CHAR) LEN(10)

  /* Initialisation correcte */
  CHGVAR     VAR(&MESSAGE) VALUE('Debut du traitement')

  /* Condition CL correcte : utiliser *EQ pour la comparaison de chaînes */
  IF         COND(&MODE *EQ '*TEST') THEN
    SNDPGMMSG MSG('Mode test')
  ENDIF

  /* Appel du programme avec ONLY les paramètres déclarés (&LIB, &USER, &MODE) 
     (remplace l'inexistant &PARAM par les bons paramètres) */
  CALL       PGM(MYLIB/MYPGM) +
             PARM(&LIB &USER &MODE)

  /* DLYJOB avec syntaxe valide : TIME attend un format hh:mm:ss ou mm:ss:uu 
     (exemple : '00:00:10' pour 10 secondes). La commande existe bien sous IBM i. */
  DLYJOB     TIME('00:00:10')

  /* Initialisation du résultat */
  CHGVAR     VAR(&RESULT) VALUE('OK')

  /* Bloc IF correctement fermé avec ENDIF */
  IF         COND(&RESULT *EQ 'OK') THEN
    SNDPGMMSG MSG('Traitement terminé')
  ENDIF

  ENDPGM
```

