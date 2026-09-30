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
