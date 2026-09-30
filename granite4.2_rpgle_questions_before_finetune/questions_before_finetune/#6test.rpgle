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