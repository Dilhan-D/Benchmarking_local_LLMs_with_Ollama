       IDENTIFICATION DIVISION.
       PROGRAM-ID. CALCUL-SALAIRE.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01 NOM-EMPLOYE     PIC X(30).
       01 SALAIRE-BRUT    PIC 9(7)V99.
       01 PRIME           PIC 9(5)V99.
       01 SALAIRE-NET     PIC 9(7)V99.
       01 TAUX-CHARGES    PIC 9V99.
       01 CHARGES         PIC 9(7)V99.

       PROCEDURE DIVISION.

       DEBUT.
           DISPLAY "Nom de l'employe : "
           ACCEPT NOM-EMPLOYE

           DISPLAY "Salaire brut : "
           ACCEPT SALAIRE-BRUT

           DISPLAY "Prime : "
           ACCEPT PRIME.

           MOVE 0.23 TO TAUX-CHARGES

           COMPUTE SALAIRE-NET =
               SALAIRE-BRUT + PRIME - CHARGES

           COMPUTE CHARGES =
               SALAIRE-BRUT * TAUX-CHARGES

           DISPLAY "Employe : " NOM-EMPLOYE
           DISPLAY "Salaire brut : " SALAIRE-BRUT
           DISPLAY "Prime : " PRIME
           DISPLAY "Charges : " CHARGES
           DISPLAY "Salaire net : " SALAIRE-NET

           STOP-RUN.