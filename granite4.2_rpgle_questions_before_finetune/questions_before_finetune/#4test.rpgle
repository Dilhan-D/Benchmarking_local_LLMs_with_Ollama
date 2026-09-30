**FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

// ERREUR 1: type de données inexistant
Dcl-S montant Float8 Inz(1000.00);  // doit être 'Dec' ou 'Packed'

// ERREUR 2: taille invalide
Dcl-S code VarChar(9999) Inz('A');  // trop grand, max 32767 mais irréaliste

// ERREUR 3: Inz avec valeur incompatible
Dcl-S age Int(3) Inz('vingt');  // doit être numérique

Dcl-S dateNaiss Date Inz(*Sys);  // OK pour comparaison

// ERREUR 4: nom de variable commence par chiffre
Dcl-S 2var Int(5);  // impossible, doit commencer par lettre

// ERREUR 5: sous-définition incorrecte
Dcl-S complexe VarChar(100);
Dcl-S partie1 Subs(complexe: 1:10);  // substr doit être %Subst

*InLR = *On;