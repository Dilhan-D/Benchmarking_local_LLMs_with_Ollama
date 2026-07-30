# Rapport de comparaison — RPGLE — Test #4

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #4 |
| Langage IBM i | RPGLE |
| Date d'exécution | 2026-07-30 |
| Numéro d'exécution | #1 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 9 |
| Lignes output (utiles) | 9 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 3 |
| Lignes modifiées | 6 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 6 |
| **Similarité globale** | **33.33%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | MODIFIEE | `**FREE` | `FREE` |
| 3 | MODIFIEE | `Dcl-S montant Float8 Inz(1000.00);  // doit être 'Dec' ou 'Packed'` | `Dcl-S montant Dec(12 2) Inz(1000.00);` |
| 4 | MODIFIEE | `Dcl-S code VarChar(9999) Inz('A');` | `Dcl-S code VarChar(20) Inz('A');` |
| 5 | MODIFIEE | `Dcl-S age Int(3) Inz('vingt');` | `Dcl-S age Int(3) Inz(20);` |
| 7 | MODIFIEE | `Dcl-S 2var Int(5);` | `Dcl-S nouvelleVar Int(5);` |
| 9 | MODIFIEE | `Dcl-S partie1 Subs(complexe: 1:10);` | `Dcl-S partie1 Subs(%Subst(complexe: 1:10));` |

## Code original (input)

```
**FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

// ERREUR 1: type de données inexistant
Dcl-S montant Float8 Inz(1000.00);  // doit être 'Dec' ou 'Packed'

// ERREUR 2: taille invalide
Dcl-S code VarChar(9999) Inz('A');  // trop grand, max 32767 mais irréaliste

// ERREUR 3: Inz avec valeur incompatible
Dcl-S age Int(3) Inz('vingt');  // doit être numérique

Dcl-S dateNaiss Date Inz(*Sys);  // OK pour comparaison

// ERREUR 4: nom de variable commence par chiffre
Dcl-S 2var Int(5);  // impossible, doit commencer par lettre

// ERREUR 5: sous-définition incorrecte
Dcl-S complexe VarChar(100);
Dcl-S partie1 Subs(complexe: 1:10);  // substr doit être %Subst

*InLR = *On;
```

## Réponse Granite — code extrait (output normalisé)

```
FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

/* Correction ERREUR 1 : Utilisation de 'Dec' au lieu de 'Float8' */
Dcl-S montant Dec(12 2) Inz(1000.00);  

/* Correction ERREUR 2 : Taille acceptable mais irréaliste, gardez la pour compatibilité, sinon réduisez-la */
Dcl-S code VarChar(20) Inz('A');  /* Exemple de taille plus raisonnable */

/* Correction ERREUR 3 : Utilisation dun entier avec une valeur numérique directe */
Dcl-S age Int(3) Inz(20);  

/* Ligne OK pour la comparaison de date */
Dcl-S dateNaiss Date Inz(*Sys);

/* Correction ERREUR 4 : Le nom de variable doit commencer par une lettre */
Dcl-S nouvelleVar Int(5);  

/* Correction ERREUR 5 : Utilisation correcte de %Subst pour extraire une sous-chaîne */
Dcl-S complexe VarChar(100);
Dcl-S partie1 Subs(%Subst(complexe: 1:10));  

*InLR = *On;
```

