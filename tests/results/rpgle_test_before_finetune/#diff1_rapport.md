# Rapport de comparaison — RPGLE — Test #1

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #1 |
| Langage IBM i | RPGLE |
| Date d'exécution | 2026-07-24 16:53:01 |
| Numéro d'exécution | #11 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 17 |
| Lignes output (utiles) | 17 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 12 |
| Lignes modifiées | 5 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 5 |
| **Similarité globale** | **70.59%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | MODIFIEE | `**FREE` | `FREE` |
| 10 | MODIFIEE | `Else` | `Else;` |
| 11 | MODIFIEE | `estMajeur = *Off` | `estMajeur = *Off;` |
| 14 | MODIFIEE | `If agee > 65;  // 'agee' n'existe pas` | `If age > 65;` |
| 17 | MODIFIEE | `salaire = salaire ** 1.10;  // '**' n'existe pas en RPGLE, doit être '*'` | `salaire = salaire * 1.10;` |

## Code original (input)

```
**FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

Dcl-S age Int(3) Inz(18);
Dcl-S nom VarChar(20) Inz('Jean');
Dcl-S salaire Dec(9 2) Inz(2500.00);  // ERREUR 1: manque virgule entre 9 et 2
Dcl-S estMajeur Ind;

// ERREUR 2: condition mal fermée (manque parenthèse)
If age >= 18;
  estMajeur = *On;
  Dsply 'Personne majeure';
Else
  // ERREUR 3: manque point-virgule après Else
  estMajeur = *Off
  Dsply 'Personne mineure';
EndIf;

// ERREUR 4: mauvais nom de variable (faute de frappe)
If agee > 65;  // 'agee' n'existe pas
  Dsply 'Senior';
EndIf;

// ERREUR 5: opérateur incorrect
salaire = salaire ** 1.10;  // '**' n'existe pas en RPGLE, doit être '*'

*InLR = *On;
```

## Réponse Granite — code extrait (output normalisé)

```
FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

Dcl-S age        Int(3) Inz(18);
Dcl-S nom        VarChar(20) Inz('Jean');
Dcl-S salaire    Dec(9 2) Inz(2500.00);  
Dcl-S estMajeur  Ind;

If age >= 18;
   estMajeur = *On;
   Dsply 'Personne majeure';
Else;
   estMajeur = *Off;
   Dsply 'Personne mineure';
EndIf;

// Correction du nom de la variable utilisée dans la condition 
If age > 65; 
   Dsply 'Senior';
EndIf;

// Utilisation d'une opération mathématique correcte pour augmenter le salaire 
   salaire = salaire * 1.10;  

*InLR = *On;
```

