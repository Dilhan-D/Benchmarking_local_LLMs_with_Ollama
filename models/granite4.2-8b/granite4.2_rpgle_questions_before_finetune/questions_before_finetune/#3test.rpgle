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