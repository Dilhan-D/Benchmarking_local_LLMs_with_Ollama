IDENTIFICATION DIVISION.
PROGRAM-ID. TEST5.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 VAL1 PIC X(3).   *> Variable alphabétique pour contenir les caractères

PROCEDURE DIVISION.
    MOVE "ABC" TO VAL1   *> Assigne la chaîne de caractères à VAL1
    DISPLAY VAL1        *> Affiche la valeur de VAL1
    STOP RUN.           *> Termine l'exécution du programme