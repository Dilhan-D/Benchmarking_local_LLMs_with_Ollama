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
