**FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

Dcl-S prix Dec(10,2) Inz(100.00);
Dcl-S quantite Int(5) Inz(10);
Dcl-S tauxTVA Dec(5,2) Inz(20.00);
Dcl-S totalHT Dec(10,2);
Dcl-S totalTTC Dec(10,2);
Dcl-S resultat Bool;

// Calculs corrects
totalHT = prix * quantite;
totalTTC = totalHT * (1 + tauxTVA / 100);

// ERREUR 1: puissance avec ^ (n'existe pas en RPGLE)
Dcl-S carre Int(10);
carre = 5 ^ 2;  // doit être '5 * 5' ou %DecFmt

// ERREUR 2: modulo avec % (incorrect)
Dcl-S reste Int(10);
reste = 10 % 3;  // doit être '%Mod(10: 3)'

// ERREUR 3: fonction %Abs mal utilisée
Dcl-S valeur Dec(10,2) Inz(-50.00);
Dcl-S absolu Dec(10,2);
absolu = %Abs valeur;  // manque parenthèses: '%Abs(valeur)'

// ERREUR 4: division par zéro potentiel
Dcl-S diviseur Dec(10,2) Inz(0);
Dcl-S quotient Dec(10,2);
quotient = totalHT / diviseur;  // Erreur runtime

// ERREUR 5: arrondi incorrect
Dcl-S arrondi Dec(10,2);
arrondi = %Round(totalTTC 2);  // manque ':', doit être '%Round(totalTTC: 2)'

// Comparaison logique
resultat = (totalHT > 1000 AND quantite >= 5);  // OK

If resultat;
  Dsply 'Commande importante';
EndIf;

*InLR = *On;