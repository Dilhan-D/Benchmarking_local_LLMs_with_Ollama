Le cycle de compilation d'un programme RPGLE (RPG - Report Program Generator) sur IBM i est un processus structuré qui transforme du code source en un programme exécutable. Voici une explication détaillée de chaque étape, ainsi que les commandes IBM i correspondantes.

1. Qu’est-ce qu’un source member ?
Un source member est une unité minimale de code source dans un source file (fichier de sources) sur IBM i. Un fichier de sources peut contenir plusieurs membres, chacun pouvant représenter un programme ou un fragment de code réutilisable.

2. Passage d’un source member à un module puis à un programme
Le passage d'un source member à un module et ensuite à un programme implique deux étapes principales :

Compilation : Le source member est compilé en un module (unité de code compilé). Pour RPGLE, cela se fait avec la commande CRTRPGMOD.

CRTRPGMOD PGM(lib/program) SRCFILE(lib/file) SRCMBR(member)
Création du programme : Un ou plusieurs modules sont liés pour former un programme exécutable. Cela est effectué par la commande CRTBNDRPG (pour RPG) ou CRTRPGPGM.

CRTBNDRPG PGM(lib/program) MODULE(module1 module2 ...)
3. Rôle de CRTBNDRPG
CRTBNDRPG est une commande IBM i utilisée pour créer un programme à partir des modules compilés. Elle gère le processus de liaison, en regroupant les modules et en résolvant les références externes (dépendances) entre eux.

4. Compilation séparée vs compilation directe
Compilation séparée : Le code source est d'abord compilé en modules indépendants, puis ces modules sont liés pour créer le programme final. Cela permet une maintenance plus facile et une réutilisation du code.

Utilisé avec CRTRPGMOD (pour la première étape) suivi de CRTBNDRPG.

Compilation directe : Le code source est compilé directement en un programme sans passer par l'étape intermédiaire des modules. C'est moins flexible mais plus rapide pour les petits programmes.

Utilisé avec CRTRPGPGM qui compile et lie le programme en une seule étape.

5. Binder source
Un binder source est un fichier de sources spécifiquement utilisé pour décrire les règles de liaison entre modules, services programs, et autres objets dans un système IBM i. Il permet de gérer des dépendances complexes et de contrôler l'environnement de liaison.

6. Gestion des dépendances entre modules
Les dépendances entre modules sont gérées via le binder source ou en spécifiant directement les modules lors de la commande de création du programme (CRTBNDRPG ou CRTRPGPGM). Les modules qui ont des dépendances mutuelles doivent être explicitement listés dans l'ordre correct pour assurer une liaison réussie.

7. Utilisation d’un copybook ou d’un service program
Lorsqu'un programme utilise un copybook (fichier de copie) ou un service program, ces éléments sont inclus via des directives de pré-compilation (/COPY pour les copybooks et /INCLUDE pour les sections spécifiques). Le système inclut le contenu du copybook au lieu de la directive, et les références externes dans le service program sont résolues lors de la liaison.

8. Diagnostic des erreurs de compilation ou de binding
Les erreurs de compilation ou de binding peuvent être diagnostiquées en examinant les messages système générés pendant le processus. Les commandes DSPMSG et RTVMSG permettent de visualiser ces messages. De plus, l'examen du journal d'erreur (WRKJOBLOG) associé à la tâche de compilation fournit des détails sur les erreurs spécifiques rencontrées.

Cycle complet avec commandes correspondantes
Création d'un source member :

ADDSRC SRCFILE(lib/file) SRCMBR(member) CCSID(1500) TEXT('Description')
Compilation en module :

CRTRPGMOD PGM(lib/program) SRCFILE(lib/file) SRCMBR(member)
Création du programme à partir des modules :

CRTBNDRPG PGM(lib/program) MODULE(module1 module2 ...)
Gestion des erreurs :

DSPMSG DLAST
Ce cycle permet de développer, compiler et déployer des programmes RPGLE sur IBM i de manière structurée et contrôlée, en assurant la maintenance du code et la résolution des dépendances.