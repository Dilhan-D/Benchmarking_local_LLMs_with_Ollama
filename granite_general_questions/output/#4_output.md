Principales notions de programmation RPG sur IBM i
1. Différence entre RPG III, RPG IV et RPGLE
RPG III : C'est la première version d'IBM pour le système iSeries (maintenant appelé IBM i). Il utilisait un format en colonnes strict et était basé sur l'assembleur.
RPG IV : Introduit pour offrir une syntaxe plus moderne et flexible. Il a ajouté des fonctionnalités comme la gestion de la mémoire automatique et a permis l'utilisation de mots-clés pour décrire les structures de données.
RPGLE (RPG Language Extension) : RPG IV a évolué vers RPGLE, qui est une extension pour supporter les langages orientés objet et les fonctionnalités avancées. RPGLE inclut des améliorations significatives comme le support des ensembles d'entrée-sortie réutilisables et la gestion des exceptions.
2. Qu’est-ce qu’un programme RPGLE ?
Un programme RPGLE est une application écrite dans le langage RPG (Report Program Generator Language Extension). Il permet de développer des solutions logicielles pour les systèmes IBM i en utilisant un ensemble riche d'instructions et de fonctions intégrées pour manipuler les données, interagir avec la base de données DB2 for i, et gérer les interfaces utilisateur.

3. Accès à DB2 for i depuis un programme RPG
Un programme RPG accède à DB2 for i en utilisant des commandes SQL directement dans le code ou via des procédures stockées. Par exemple :

DCL-F FILENAME IFSPROC;
EXEC SQL DECLARE C CURSOR FOR 
    SELECT * FROM TABLE_NAME WHERE CONDITION;
Ici, EXEC SQL permet d'inclure du code SQL directement dans le programme RPG.

4. Rôle des fichiers déclarés dans un programme RPG
Les fichiers déclarés dans un programme RPG servent à spécifier comment et où les données sont lues ou écrites. Ils incluent les types de fichiers (physique, clinique, séquentiel, etc.), le mode d'accès (lecture, écriture, mise à jour), et les clés pour les recherches par index.

5. Différence entre free-form RPG et l’ancien format en colonnes
Free-form RPG : Permet une syntaxe plus flexible où les instructions peuvent être écrites sur n'importe quelle ligne sans respecter de contraintes strictes de colonnes. Cela améliore la lisibilité et facilite le développement.
Format en colonnes : Utilise des positions fixes pour chaque type d'instruction (par exemple, l'instruction C doit commencer à la colonne 6). C'est plus rigide mais était nécessaire pour les premières versions d'RPG.
6. Appel d'un autre programme ou d'une procédure depuis un programme RPG
Un programme RPG peut appeler un autre programme ou une procédure en utilisant l'instruction CALL. Par exemple :

C     CALL 'PROGNAME'
Pour appeler une procédure spécifique dans un programme, vous pouvez utiliser :

C     CALLP PROCEDURE_NAME(parameters)
7. Gestion des erreurs et des exceptions dans un programme RPGLE
La gestion des erreurs et des exceptions est gérée principalement via le bloc EXCEPT. Voici un exemple simple :

EXCEPT;
   MONITOR;
      EXEC SQL INSERT INTO TABLE_NAME VALUES (:VARIABLE1, :VARIABLE2);
   ENDMON;
   WHEN-EXCP-01;
      // Gérer l'erreur d'entrée en double ou autre erreur spécifique
ENDMRG;
Exemples simples de code RPGLE
Exemple 1 : Lecture et écriture dans un fichier
**free
H DFTACTGRP(*NO)
PGMNAM(READFILE)

DCL-S filename CHAR(20);
DCL-F MYFILE DISK USRCTRL;

filename = 'DATAFILE';

OVRDBF FILE(MYFILE) TOFILE(QTEMP/TEMPFILE);

FRCESTR(INDEXKEYS(*ALL));

// Lecture
READ myFile REC(recData);

// Traitement des données
...

// Écriture
WRITE myFile REC(recData);
Exemple 2 : Appel d'une procédure dans un autre programme
**free
PGMNAM(CALLPROC)

DCL-S inputParm INT(10) INZ(5);
DCL-PI *ENTRY PARM(inputParm);
    
CALLP PROGNAME/PROCNAME(inputParm);

ENDPGM;
Exemple 3 : Gestion d'une exception SQL
**free
H DFTACTGRP(*NO)
PGMNAM(EXCEPTION)

EXEC SQL CONNECT TO DATABASE_NAME USING ;
BEGIN-EXCEPT;

   EXEC SQL INSERT INTO TABLE_NAME VALUES (:variable1, :variable2);

ENDEXCEPT;

WHEN-EXCP-01;
   // Gestion d'une erreur d'entrée en double
   EXEC SQL ROLLBACK;  
ENDMRG;
Ces exemples illustrent les bases de la programmation RPGLE sur IBM i, couvrant des opérations courantes comme l'accès aux fichiers, le traitement des données, et la gestion des exceptions.