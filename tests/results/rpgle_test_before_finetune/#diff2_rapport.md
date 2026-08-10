# Rapport de comparaison — RPGLE — Test #2

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #2 |
| Langage IBM i | RPGLE |
| Date d'exécution | 2026-07-30 |
| Numéro d'exécution | #1 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 14 |
| Lignes output (utiles) | 14 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 13 |
| Lignes modifiées | 1 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 1 |
| **Similarité globale** | **92.86%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | MODIFIEE | `**FREE` | `FREE` |

## Code original (input)

```
**FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

Dcl-S compteur Int(5) Inz(0);
Dcl-S total Dec(10 2) Inz(0); 
Dcl-S nombre Int(10);

For compteur = 1 To 10;
  total += compteur;
EndFor

compteur = 0;
Dow compteur < 5;
  compteur += 1;
EndDo;

total += extra; 

Dsply 'Termine';
*InLR = *On;
```

## Réponse Granite — code extrait (output normalisé)

```
FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

Dcl-S compteur    Int(5) Inz(0);
Dcl-S total       Dec(10 2) Inz(0); 
Dcl-S nombre      Int(10);

/* Boucle For pour sommer les nombres de 1 à 10 */
For compteur = 1 To 10;
   total += compteur;
EndFor

/* Initialisation de compteur à 0 et boucle Dow jusqu'à ce qu'il atteigne 5 */
compteur = 0;
Dow compteur < 5;
   compteur += 1;
EndDo;

/* Correction : la variable 'extra' n'est pas définie, utilisez une autre variable ou initialisez-la */
total += extra; /* Cette ligne doit être corrigée pour éviter une erreur de compilation */

/* Affichage et fin du programme */
Dsply 'Termine';
*InLR = *On;
```

