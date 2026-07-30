# Rapport de comparaison — RPGLE — Test #6

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #6 |
| Langage IBM i | RPGLE |
| Date d'exécution | 2026-07-30 |
| Numéro d'exécution | #1 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 34 |
| Lignes output (utiles) | 33 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 24 |
| Lignes modifiées | 9 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 2 |
| Total différences | 11 |
| **Similarité globale** | **70.59%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | MODIFIEE | `**FREE` | `FREE` |
| 2 | MODIFIEE | `Ctl-Opt DftActGrp(*No) ActGrp(*Caller);` | `Ctl-Opt DftActGrp(*NO) ActGrp(*CALLER);` |
| 7 | MODIFIEE | `Dcl-S estEmploye Bool Inz(*On);` | `Dcl-S estEmploye Bool Inz(*ON);` |
| 8 | MODIFIEE | `If age >= 18 AND age < 65 && salaire >= 2000;  // '&&' n'existe, doit être 'AND'` | `If age >= 18 AND age < 65 AND salaire >= 2000;` |
| 11 | MODIFIEE | `If NOT(age < 18);` | `If age >= 18;` |
| 14 | MODIFIEE | `If (age >= 18 AND age < 65 OR salaire >= 5000;  // manque ')'` | `If (age >= 18 AND age < 65) OR salaire >= 5000;` |
| 17 | MODIFIEE | `If salaire = '2500';` | `Dcl-S salaireNum Int(10);` |
| 18 | MODIFIEE | `` | `salaireNum = %Dec(salaire, 10, 2);` |
| 28 | SUPPRIMEE | `If age > 30;` | `` |
| 29 | SUPPRIMEE | `prime = 1000;` | `` |
| 33 | MODIFIEE | `If salaire = NULL;  // doit être 'salaire = *Null' ou 'IsNull(salaire)'` | `If salaireNum <> *BLANK;` |

## Code original (input)

```
**FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

Dcl-S age Int(3) Inz(25);
Dcl-S salaire Dec(10,2) Inz(2500.00);
Dcl-S categorie VarChar(20);
Dcl-S prime Dec(10,2);
Dcl-S estEmploye Bool Inz(*On);

// ERREUR 1: AND/OR mal orthographié
If age >= 18 AND age < 65 && salaire >= 2000;  // '&&' n'existe, doit être 'AND'
  categorie = 'Actif';
EndIf;

// ERREUR 2: NOT mal utilisé
If NOT(age < 18);  // OK mais peut être simplifié
  Dsply 'Majeur';
EndIf;

// ERREUR 3: parenthèse manquante dans condition complexe
If (age >= 18 AND age < 65 OR salaire >= 5000;  // manque ')'
  categorie = 'Prioritaire';
EndIf;

// ERREUR 4: comparaison de chaîne avec nombre
If salaire = '2500';  // doit être numérique, pas chaîne

// SELECT avec erreurs
Select;
  // ERREUR 5: When mal orthographié
  Whene age < 18;
    categorie = 'Mineur';
  
  // ERREUR 6: When sans condition
  When;
    categorie = 'Inconnu';
  
  // ERREUR 7: Other mal orthographié
  Othr;
    categorie = 'Autre';
EndSelect;

// ERREUR 8: If sans EndIf
If age > 30;
  prime = 1000;
// manque EndIf

// Correction
If age > 30;
  prime = 1000;
Else;
  prime = 500;
EndIf;

// ERREUR 9: Test de null incorrect
If salaire = NULL;  // doit être 'salaire = *Null' ou 'IsNull(salaire)'

Dsply 'Categorie : ' + categorie;
*InLR = *On;
```

## Réponse Granite — code extrait (output normalisé)

```
FREE
Ctl-Opt DftActGrp(*NO) ActGrp(*CALLER);

Dcl-S age Int(3) Inz(25);
Dcl-S salaire Dec(10,2) Inz(2500.00);
Dcl-S categorie VarChar(20);
Dcl-S prime Dec(10,2);
Dcl-S estEmploye Bool Inz(*ON);  // *ON au lieu de *On pour la casse

// Condition corrigée avec 'AND'
If age >= 18 AND age < 65 AND salaire >= 2000;
  categorie = 'Actif';
EndIf;

// Simplification de la condition
If age >= 18;
  Dsply 'Majeur';
EndIf;

// Ajout de la parenthèse manquante et correction du type de données pour salaire
If (age >= 18 AND age < 65) OR salaire >= 5000;
  categorie = 'Prioritaire';
EndIf;

// Utilisation numérique pour salaire
Dcl-S salaireNum Int(10);
salaireNum = %Dec(salaire, 10, 2);

Select;
  Whene age < 18;
    categorie = 'Mineur';
  
  When;
    categorie = 'Inconnu';
  
  Othr;
    categorie = 'Autre';
EndSelect;

// Simplification des conditions pour prime
If age > 30;
  prime = 1000;
Else;
  prime = 500;
EndIf;

// Vérification de NULL (en RPGLE, on vérifie généralement avec une condition numérique ou caractère appropriée)
If salaireNum <> *BLANK;  // Exemple de vérification pour un champ numérique

Dsply 'Categorie : ' + categorie;
*InLR = *ON;  // *ON au lieu de *On pour la casse
```

