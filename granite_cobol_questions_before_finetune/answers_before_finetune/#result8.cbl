       IDENTIFICATION DIVISION.
       PROGRAM-ID. CLIENT01.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.

       FILE-CONTROL.
           SELECT DSPF-CLIENT
               ASSIGN TO WORKSTATION-GESTION.

       DATA DIVISION.
       FILE SECTION.
       
       COPY DDS-ALL-FORMATS OF DSPF-CLIENT INTO DSPF-CLIENT.  -- Inclure les formats du fichier DDS

       FD DSPF-CLIENT.
       01 CLIENT-SCREEN.
           INCLUDE DDS-ALL-FORMATS.  -- Inclure les formats dans la définition de fichier

       WORKING-STORAGE SECTION.
       01 WS-NOM       PIC X(30).
       01 WS-CHOIX     PIC X.

       PROCEDURE DIVISION.

           OPEN I-O DSPF-CLIENT

           MOVE "Dupont" TO WS-NOM
           MOVE "1" TO WS-CHOIX

           -- Utilisez le format approprié pour écrire sur l'écran
           WRITE CLIENT-SCREEN FORMAT "CLIENT"

           CLOSE DSPF-CLIENT

           STOP RUN.
