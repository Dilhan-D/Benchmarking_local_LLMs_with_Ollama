        IDENTIFICATION DIVISION.
        PROGRAM-ID. TEST6.

        DATA DIVISION.
        WORKING-STORAGE SECTION.
        01 COUNTER PIC 9(2).  * Utilisez un format de numération approprié pour le compteur.
        10 VENOM   PIC X(1).  * Assurez-vous que la longueur de VENOM est spécifiée correctement.

        PROCEDURE DIVISION.
            PERFORM 3 TIMES
                DISPLAY "ERROR"  * Remplacez PRINT par DISPLAY pour afficher du texte.
            END-PERFORM.
            COMPUTE COUNTER = COUNTER + 1.  * Corrigez la ligne COMPUTE pour qu'elle utilise le compteur correctement.
            STOP RUN.
