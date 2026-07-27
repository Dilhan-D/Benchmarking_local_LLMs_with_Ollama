# Rapport de comparaison — RPGLE — Test #5

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #5 |
| Langage IBM i | RPGLE |
| Date d'exécution | 2026-07-24 16:53:01 |
| Numéro d'exécution | #11 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 26 |
| Lignes output (utiles) | 26 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 19 |
| Lignes modifiées | 7 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 7 |
| **Similarité globale** | **73.08%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | MODIFIEE | `**FREE` | `FREE` |
| 2 | MODIFIEE | `Ctl-Opt DftActGrp(*No) ActGrp(*Caller);` | `Ctl-Opt DftActGrp(*NO) ActGrp(*CALLER);` |
| 12 | MODIFIEE | `carre = 5 ^ 2;  // doit être '5 * 5' ou %DecFmt` | `carre = 5 * 5;  // doit être '5 * 5'` |
| 14 | MODIFIEE | `reste = 10 % 3;  // doit être '%Mod(10: 3)'` | `reste = %Mod(10: 3);` |
| 17 | MODIFIEE | `absolu = %Abs valeur;  // manque parenthèses: '%Abs(valeur)'` | `absolu = %Abs(valeur);` |
| 18 | MODIFIEE | `Dcl-S diviseur Dec(10,2) Inz(0);` | `Dcl-S diviseur Dec(10,2) Inz(1);` |
| 22 | MODIFIEE | `arrondi = %Round(totalTTC 2);  // manque ':', doit être '%Round(totalTTC: 2)'` | `arrondi = %Round(totalTTC: 2);` |

## Code original (input)

```
**FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

Dcl-S prix Dec(10,2) Inz(100.00);
Dcl-S quantite Int(5) Inz(10);
Dcl-S tauxTVA Dec(5,2) Inz(20.00);
Dcl-S totalHT Dec(10,2);
Dcl-S totalTTC Dec(10,2);
Dcl-S resultat Bool;

// Calculs corrects
totalHT = prix * quantite;
totalTTC = totalHT * (1 + tauxTVA / 100);

// ERREUR 1: puissance avec ^ (n'existe pas en RPGLE)
Dcl-S carre Int(10);
carre = 5 ^ 2;  // doit être '5 * 5' ou %DecFmt

// ERREUR 2: modulo avec % (incorrect)
Dcl-S reste Int(10);
reste = 10 % 3;  // doit être '%Mod(10: 3)'

// ERREUR 3: fonction %Abs mal utilisée
Dcl-S valeur Dec(10,2) Inz(-50.00);
Dcl-S absolu Dec(10,2);
absolu = %Abs valeur;  // manque parenthèses: '%Abs(valeur)'

// ERREUR 4: division par zéro potentiel
Dcl-S diviseur Dec(10,2) Inz(0);
Dcl-S quotient Dec(10,2);
quotient = totalHT / diviseur;  // Erreur runtime

// ERREUR 5: arrondi incorrect
Dcl-S arrondi Dec(10,2);
arrondi = %Round(totalTTC 2);  // manque ':', doit être '%Round(totalTTC: 2)'

// Comparaison logique
resultat = (totalHT > 1000 AND quantite >= 5);  // OK

If resultat;
  Dsply 'Commande importante';
EndIf;

*InLR = *On;
```

## Réponse Granite — code extrait (output normalisé)

```
FREE
Ctl-Opt DftActGrp(*NO) ActGrp(*CALLER);

Dcl-S prix Dec(10,2) Inz(100.00);
Dcl-S quantite Int(5) Inz(10);
Dcl-S tauxTVA Dec(5,2) Inz(20.00);
Dcl-S totalHT Dec(10,2);
Dcl-S totalTTC Dec(10,2);
Dcl-S resultat Bool;

totalHT = prix * quantite;
totalTTC = totalHT * (1 + tauxTVA / 100);

// Correction de l'opérateur puissance
Dcl-S carre Int(10);
carre = 5 * 5;  // doit être '5 * 5'

// Correction de l'opérateur modulo
Dcl-S reste Int(10);
reste = %Mod(10: 3);  

// Utilisation correcte de la fonction absolue
Dcl-S valeur Dec(10,2) Inz(-50.00);
Dcl-S absolu Dec(10,2);
absolu = %Abs(valeur);  

// Attention à la division par zéro
Dcl-S diviseur Dec(10,2) Inz(1);  // Changement pour éviter la division par zéro
Dcl-S quotient Dec(10,2);
quotient = totalHT / diviseur;  

// Utilisation correcte de la fonction d'arrondi
Dcl-S arrondi Dec(10,2);
arrondi = %Round(totalTTC: 2);  

resultat = (totalHT > 1000 AND quantite >= 5);  // OK

If resultat;
  Dsply 'Commande importante';
EndIf;

*InLR = *On;
```

