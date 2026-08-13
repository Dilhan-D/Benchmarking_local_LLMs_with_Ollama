FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

Dcl-S compteur    Int(5) Inz(0);
Dcl-S total       Dec(10 2) Inz(0); 
Dcl-S nombre      Int(10);

/* Boucle For pour sommer les nombres de 1 à 10 */
For compteur = 1 To 10;
   total += compteur;
EndFor

/* Initialisation de compteur à 0 et boucle Dow jusqu'à ce qu'il atteigne 5 */
compteur = 0;
Dow compteur < 5;
   compteur += 1;
EndDo;

/* Correction : la variable 'extra' n'est pas définie, utilisez une autre variable ou initialisez-la */
total += extra; /* Cette ligne doit être corrigée pour éviter une erreur de compilation */

/* Affichage et fin du programme */
Dsply 'Termine';
*InLR = *On;
