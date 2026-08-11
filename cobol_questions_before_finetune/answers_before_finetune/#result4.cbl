IDENTIFICATION DIVISION.
PROGRAM-ID. TEST4.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 COUNTER PIC 9(2) VALUE 0.   *> Déclare un compteur de 2 chiffres, initialisé à 0

PROCEDURE DIVISION.
    PERFORM UNTIL COUNTER > 5      *> Boucle jusqu'à ce que le compteur soit supérieur à 5
        DISPLAY COUNTER            *> Affiche la valeur actuelle du compteur
        ADD 1 TO COUNTER           *> Incrément le compteur de 1
    END-PERFORM.
STOP RUN.                         *> Termine l'exécution du programme
