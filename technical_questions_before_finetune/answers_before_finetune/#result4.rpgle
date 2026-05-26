FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

/* Correction ERREUR 1 : Utilisation de 'Dec' au lieu de 'Float8' */
Dcl-S montant Dec(12 2) Inz(1000.00);  

/* Correction ERREUR 2 : Taille acceptable mais irréaliste, gardez la pour compatibilité, sinon réduisez-la */
Dcl-S code VarChar(20) Inz('A');  /* Exemple de taille plus raisonnable */

/* Correction ERREUR 3 : Utilisation dun entier avec une valeur numérique directe */
Dcl-S age Int(3) Inz(20);  

/* Ligne OK pour la comparaison de date */
Dcl-S dateNaiss Date Inz(*Sys);

/* Correction ERREUR 4 : Le nom de variable doit commencer par une lettre */
Dcl-S nouvelleVar Int(5);  

/* Correction ERREUR 5 : Utilisation correcte de %Subst pour extraire une sous-chaîne */
Dcl-S complexe VarChar(100);
Dcl-S partie1 Subs(%Subst(complexe: 1:10));  

*InLR = *On;
