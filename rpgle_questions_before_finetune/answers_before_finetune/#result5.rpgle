FREE
Ctl-Opt DftActGrp(*NO) ActGrp(*CALLER);

Dcl-S prix Dec(10,2) Inz(100.00);
Dcl-S quantite Int(5) Inz(10);
Dcl-S tauxTVA Dec(5,2) Inz(20.00);
Dcl-S totalHT Dec(10,2);
Dcl-S totalTTC Dec(10,2);
Dcl-S resultat Bool;

totalHT = prix * quantite;
totalTTC = totalHT * (1 + tauxTVA / 100);

// Correction de l'opérateur puissance
Dcl-S carre Int(10);
carre = 5 * 5;  // doit être '5 * 5'

// Correction de l'opérateur modulo
Dcl-S reste Int(10);
reste = %Mod(10: 3);  

// Utilisation correcte de la fonction absolue
Dcl-S valeur Dec(10,2) Inz(-50.00);
Dcl-S absolu Dec(10,2);
absolu = %Abs(valeur);  

// Attention à la division par zéro
Dcl-S diviseur Dec(10,2) Inz(1);  // Changement pour éviter la division par zéro
Dcl-S quotient Dec(10,2);
quotient = totalHT / diviseur;  

// Utilisation correcte de la fonction d'arrondi
Dcl-S arrondi Dec(10,2);
arrondi = %Round(totalTTC: 2);  

resultat = (totalHT > 1000 AND quantite >= 5);  // OK

If resultat;
  Dsply 'Commande importante';
EndIf;

*InLR = *On;
