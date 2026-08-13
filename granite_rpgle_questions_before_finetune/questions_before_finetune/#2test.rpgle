**FREE
Ctl-Opt DftActGrp(*No) ActGrp(*Caller);

Dcl-S compteur Int(5) Inz(0);
Dcl-S total Dec(10 2) Inz(0); 
Dcl-S nombre Int(10);

For compteur = 1 To 10;
  total += compteur;
EndFor

compteur = 0;
Dow compteur < 5;
  compteur += 1;
EndDo;

total += extra; 

Dsply 'Termine';
*InLR = *On;