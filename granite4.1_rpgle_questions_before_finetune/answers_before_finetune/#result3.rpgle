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
