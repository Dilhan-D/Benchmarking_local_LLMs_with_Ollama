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
