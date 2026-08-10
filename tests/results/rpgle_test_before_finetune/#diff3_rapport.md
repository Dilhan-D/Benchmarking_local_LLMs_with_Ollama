# Rapport de comparaison — RPGLE — Test #3

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #3 |
| Langage IBM i | RPGLE |
| Date d'exécution | 2026-07-30 |
| Numéro d'exécution | #1 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 16 |
| Lignes output (utiles) | 17 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 11 |
| Lignes modifiées | 6 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 6 |
| **Similarité globale** | **68.75%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 1 | MODIFIEE | `**FREE` | `FREE` |
| 5 | MODIFIEE | `Whene note >= 90;` | `Select;` |
| 6 | MODIFIEE | `` | `When note >= 90;` |
| 12 | MODIFIEE | `resultat = 'Echec'` | `resultat = 'Echec';` |
| 13 | MODIFIEE | `EndSelect;` | `EndSel;` |
| 14 | MODIFIEE | `If note =/> 0;  // doit être '<=' ou '>=', pas '=/>'` | `If note > 0;` |

## Code original (input)

```
**FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

Dcl-S note Int(3) Inz(75);
Dcl-S resultat VarChar(20);

// ERREUR 1: When mal orthographié
Whene note >= 90;
  resultat = 'Excellent';
When note >= 75;
  resultat = 'Bien';
When note >= 50;
  resultat = 'Moyen';
Other
  // ERREUR 2: manque point-virgule après Other
  resultat = 'Echec'  // ERREUR 3: manque point-virgule
EndSelect;  // ERREUR 4: mal orthographié (EndSelect au lieu de EndIf ou erreur de nom)

// ERREUR 5: opérateur de comparaison incorrect
If note =/> 0;  // doit être '<=' ou '>=', pas '=/>'
  Dsply 'Note valide';
EndIf;

*InLR = *On;
```

## Réponse Granite — code extrait (output normalisé)

```
FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

Dcl-S note        Int(3) Inz(75);
Dcl-S resultat    VarChar(20);

/* Utilisation de la structure When pour déterminer le résultat en fonction de la note */
Select;
  When note >= 90;
     resultat = 'Excellent';
  When note >= 75;
     resultat = 'Bien';
  When note >= 50;
     resultat = 'Moyen';
  Other
     resultat = 'Echec';
EndSel;

/* Correction de l'opérateur dans la condition If : '/' ne doit pas être utilisé avec '=' */
If note > 0;  
   Dsply 'Note valide';
EndIf;

*InLR = *On;
```

