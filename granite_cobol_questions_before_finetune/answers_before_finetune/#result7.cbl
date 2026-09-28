       IDENTIFICATION DIVISION.
       PROGRAM-ID. CALCUL-SALAIRE.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01 NOM-EMPLOYE     PIC X(30).
       01 SALAIRE-BRUT    PIC 9(7)V99.
       01 PRIME           PIC 9(5)V99.
       01 SALAIRE-NET     PIC 9(7)V99.
       01 TAUX-CHARGES    PIC 9V99 VALUE 23.   *> Initialise le taux de charges à 23%
       01 CHARGES         PIC 9(7)V99.

       PROCEDURE DIVISION.

       DEBUT.
           DISPLAY "Nom de l'employé : "
           ACCEPT NOM-EMPLOYE

           DISPLAY "Salaire brut : "
           ACCEPT SALAIRE-BRUT

           DISPLAY "Prime : "
           ACCEPT PRIME

           *> Calcul des charges
           COMPUTE CHARGES = SALAIRE-BRUT * TAUX-CHARGES / 100

           *> Calcul du salaire net
           COMPUTE SALAIRE-NET = SALAIRE-BRUT + PRIME - CHARGES

           DISPLAY "Employé : " NOM-EMPLOYE
           DISPLAY "Salaire brut : " SALAIRE-BRUT
           DISPLAY "Prime : " PRIME
           DISPLAY "Charges : " CHARGES
           DISPLAY "Salaire net : " SALAIRE-NET

           STOP-RUN.
