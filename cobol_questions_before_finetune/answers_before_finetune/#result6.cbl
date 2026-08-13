        IDENTIFICATION DIVISION.
        PROGRAM-ID. TEST6.

        DATA DIVISION.
        WORKING-STORAGE SECTION.
        01 COUNTER PIC 9(2).  
        10 VENOM   PIC X(1). 

        PROCEDURE DIVISION.
            PERFORM 3 TIMES
                DISPLAY "ERROR" 
            END-PERFORM.
            COMPUTE COUNTER = COUNTER + 1.  
            STOP RUN.
