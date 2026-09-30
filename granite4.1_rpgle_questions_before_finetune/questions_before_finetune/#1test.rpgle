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