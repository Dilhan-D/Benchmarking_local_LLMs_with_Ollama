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
  
End-Sub;  // ERREUR 3: 'End-Sub' au lieu de 'End-Proc'

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