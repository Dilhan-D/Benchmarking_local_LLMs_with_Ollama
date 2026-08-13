# Rapport de comparaison — RPGLE — Test #7

## Informations générales

| Champ | Valeur |
|---|---|
| Test | #7 |
| Langage IBM i | RPGLE |
| Date d'exécution | 2026-08-13 |
| Numéro d'exécution | #1 |
| Modèle utilisé | granite4.1:8b |
| Lignes input (utiles) | 36 |
| Lignes output (utiles) | 35 |
| Méthode d'extraction | Heuristique (aucun bloc trouvé) |
| Méthode de comparaison | Alignement difflib (SequenceMatcher) |
| Commentaires ignorés | True |
| Casse ignorée | False |
| Indentation ignorée | Toujours (aucune valeur syntaxique en IBM i) |

## Statistiques de comparaison

| Métrique | Valeur |
|---|---|
| Lignes identiques | 21 |
| Lignes modifiées | 15 |
| Lignes ajoutées | 0 |
| Lignes supprimées | 0 |
| Total différences | 15 |
| **Similarité globale** | **58.33%** |

## Différences détectées

| Ligne | Type | Avant | Après |
|---|---|---|---|
| 2 | MODIFIEE | `Ctl-Opt DftActGrp(*No) ActGrp(*Caller);` | `Ctl-Opt DftActGrp(*NO) ActGrp(*CALLER);` |
| 4 | MODIFIEE | `Dcl-Pr Calculer ExtpProc('CALCULER');  // doit être 'ExtProc'` | `Dcl-Pr Calculer ExtpProc('CALCULER');` |
| 8 | MODIFIEE | `resultat = Calculer(10: 20);` | `resultat = Calculer(10: 20);  // Supposons que CALCULER retourne une valeur compatible avec 'resultat'` |
| 10 | MODIFIEE | `Dcl-SubProc MonSousProc;  // doit être 'Dcl-Proc'` | `Dcl-SubProc MonSousProc;` |
| 11 | MODIFIEE | `Dcl-Pi MonSousProc;` | `Dcl-Pi MonSousProc param1 Int(10);` |
| 12 | MODIFIEE | `param1 Int(10);` | `Dsply 'Sous-procédure appelée avec param1 = ' + %Char(param1);` |
| 14 | MODIFIEE | `Dsply 'Sous-procédure appelée';` | `End-Sub;` |
| 15 | MODIFIEE | `End-Sub;  // ERREUR 3 : 'End-Sub' au lieu de 'End-Proc'` | `` |
| 17 | MODIFIEE | `Dcl-Proc ProcInterne;` | `Dcl-Proc ProcInterne InLb;  // Utilisez InLb pour indiquer que c'est une procédure locale` |
| 22 | MODIFIEE | `Return ProcInterne();` | `Dsply 'Resultat de ProcInterne : ' + %Dec(ProcInterne(), 10, 2);` |
| 26 | MODIFIEE | `salaireBase Dec(10,2);` | `salaireBase Dec(10,2) ;` |
| 28 | MODIFIEE | `End-PI;` | `End-Pi;` |
| 33 | MODIFIEE | `End-PI;` | `End-Pi;` |
| 34 | MODIFIEE | `End-Proc Export;` | `End-Proc;  // Utilisez 'N' à la place de 'Export' pour une procédure non exportée` |
| 35 | MODIFIEE | `CallP Calculer(10: 20);  // doit être 'Calculer(10: 20)'` | `CallP Calculer(10: 20);` |

## Code original (input)

```
**FREE
// Module Principal
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

Dcl-S resultat Int(10);

// ERREUR 1: ExtpProc mal orthographié
Dcl-Pr Calculer ExtpProc('CALCULER');  // doit être 'ExtProc'
  a Int(10);
  b Int(10);
End-Pr;

resultat = Calculer(10: 20);
Dsply 'Resultat : ' + %Char(resultat);

// ERREUR 2: Dcl-SubProc au lieu de Dcl-Proc
Dcl-SubProc MonSousProc;  // doit être 'Dcl-Proc'
  Dcl-Pi MonSousProc;
    param1 Int(10);
  End-PI;
  
  Dsply 'Sous-procédure appelée';
  
End-Sub;  // ERREUR 3 : 'End-Sub' au lieu de 'End-Proc'

// ERREUR 4: Procédure dans procédure (impossible)
Dcl-Proc ProcExterne;
  Dcl-Proc ProcInterne;  // Impossible, procédure imbriquée
    Dcl-Pi ProcInterne;
    End-PI;
    Return 42;
  End-Proc;
  
  Return ProcInterne();
End-Proc;

// Bonnes pratiques
Dcl-Proc CalculerSalaire Export;
  Dcl-Pi CalculerSalaire Dec(10,2);
    salaireBase Dec(10,2);
    taux Dec(5,2);
  End-PI;
  
  Return salaireBase * (1 + taux / 100);
  
End-Proc;

// ERREUR 5: Export sur procédure sans prototype
Dcl-Proc ProcNonExport;
  Dcl-Pi ProcNonExport;
  End-PI;
End-Proc Export;  // Export mal placé (doit être sur Dcl-Proc)

// ERREUR 6: CallP sur procédure locale (doit être appel direct)
CallP Calculer(10: 20);  // doit être 'Calculer(10: 20)'

MonSousProc(100);

*InLR = *On;
```

## Réponse Granite — code extrait (output normalisé)

```
**FREE

Ctl-Opt DftActGrp(*NO) ActGrp(*CALLER);

Dcl-S resultat Int(10);

// Définition de la procédure externe CALCULER
Dcl-Pr Calculer ExtpProc('CALCULER');
  a Int(10);
  b Int(10);
End-Pr;

resultat = Calculer(10: 20);  // Supposons que CALCULER retourne une valeur compatible avec 'resultat'
Dsply 'Resultat : ' + %Char(resultat);

// Définition de la sous-procédure MonSousProc
Dcl-SubProc MonSousProc;
  Dcl-Pi MonSousProc param1 Int(10);
    Dsply 'Sous-procédure appelée avec param1 = ' + %Char(param1);
  End-PI;
End-Sub;

// Définition de la procédure ProcExterne contenant une procédure interne
Dcl-Proc ProcExterne;
  Dcl-Proc ProcInterne InLb;  // Utilisez InLb pour indiquer que c'est une procédure locale
    Dcl-Pi ProcInterne;
    End-PI;
    Return 42;
  End-Proc;

  // Appel de la procédure interne depuis ProcExterne
  Dsply 'Resultat de ProcInterne : ' + %Dec(ProcInterne(), 10, 2);
End-Proc;

// Définition de la procédure CalculerSalaire exportée
Dcl-Proc CalculerSalaire Export;
  Dcl-Pi CalculerSalaire Dec(10,2);
    salaireBase Dec(10,2) ;
    taux      Dec(5,2);
  End-Pi;

  // Calcul du salaire total avec la prime
  Return salaireBase * (1 + taux / 100);
  
End-Proc;

// Procédure non exportée
Dcl-Proc ProcNonExport;
  Dcl-Pi ProcNonExport;
  End-Pi;
End-Proc;  // Utilisez 'N' à la place de 'Export' pour une procédure non exportée

CallP Calculer(10: 20);  // Assurez-vous que CALCULER est définie correctement en dehors du module

MonSousProc(100);

*InLR = *ON;  // *ON au lieu de *On pour la casse
```

