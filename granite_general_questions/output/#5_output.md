Le système d'objets IBM i est une caractéristique fondamentale de l'architecture du système d'exploitation IBM i, qui repose sur la plateforme AS/400. Ce concept est essentiel pour comprendre comment le système gère les ressources et les programmes. Voici une explication détaillée :

Qu’est-ce qu’un objet IBM i ?
Un objet IBM i est une entité stockée dans le système qui peut être un fichier, un programme, une autorisation, une tâche en attente ou toute autre ressource manipulable par le système. Chaque objet possède des attributs qui définissent son type, sa taille, ses droits d'accès et bien plus encore.

Quels sont les principaux types d’objets que l’on rencontre ?
Les principaux types d'objets incluent :

PF (Physical File) : Fichiers contenant des données brutes.
LF (Logical File) : Fichiers qui fournissent un accès à des PF avec une vue différente ou filtrée.
PGM (Program) : Programme exécutable, écrit en langage de programmation comme RPG ou COBOL.
SRVPGM (Service Program) : Ensemble de procédures réutilisables exposées à d'autres programmes.
DTAQ (Data Queue) : Structure pour le stockage temporaire des messages entre processus.
JOBQ (Job Queue) : File d'attente pour les travaux en attente d'exécution.
Quelle différence entre un objet PF, LF, PGM, SRVPGM, DTAQ et JOBQ ?
PF est utilisé pour stocker des données de manière structurée.
LF offre une interface filtrée ou réorganisée sur les PF sans modifier les données physiques.
PGM contient le code exécutable d'une application.
SRVPGM regroupe des fonctions réutilisables, souvent appelées par plusieurs programmes.
DTAQ permet l'échange de messages entre processus ou applications.
JOBQ gère la priorité et l'exécution des tâches dans le système.
Comment IBM i identifie-t-il un objet ?
IBM i utilise une combinaison du nom de l'objet, du nom du libellé d'unité de stockage (library) et, si nécessaire, du système de fichiers pour identifier unique chaque objet. Par exemple, MYLIB/MYFILE désigne un fichier PF nommé MYFILE dans la bibliothèque MYLIB.

Pourquoi IBM i utilise-t-il une architecture basée sur les objets ?
L'architecture objet fournit une isolation des ressources, facilitant le partage, la sécurité et la gestion des modifications. Elle permet également un déploiement modulaire où les composants peuvent être mis à jour ou remplacés sans affecter l'ensemble du système.

Comment copier, déplacer ou supprimer un objet ?
Copier : CPY OBJ FROMOBJ(mylib/myobj) TOOBJ(newlib/newobj)
Déplacer : MVPE OBJ FROMOBJ(mylib/myobj) TOOBJ(newlib/newobj)
Supprimer : DLTOBJ OBJ(mylib/myobj)
Que se passe-t-il lorsqu’un programme dépend d’autres objets ?
Lorsque un programme (par exemple, un PGM) dépend d'autres objets (comme des PF ou SRVPGM), IBM i vérifie l'existence et les droits d'accès à ces objets au moment de l'exécution. Si un objet requis est absent ou inaccessible, le programme échoue avec une erreur indiquant la nature du problème.

Exemples concrets avec les commandes CL correspondantes
Créer un fichier physique (PF) :

CRTPF FILE(MYLIB/MYFILE) RCDLEN(100)
Créer une vue logique (LF) sur le PF créé :

CRTLF FILE(MYLIB/MYVIEW) LF(MYLIB/MYFILE)
Copier un programme existant dans une nouvelle bibliothèque :

CPY OBJ FROMOBJ(QSYS/QCMD) TOOBJ(MYLIB/NEWQCMD)
Supprimer une file d’attente de travail (JOBQ) :

DLTOBJ OBJ(MYLIB/MYJOBQ)
Déplacer un fichier LF vers une nouvelle bibliothèque :

MVPE OBJ FROMOBJ(MYLIB/OLDVIEW) TOOBJ(newlib/newview)
Ces commandes CL (Command Language) facilitent la gestion des objets, démontrant comment IBM i permet une manipulation précise et contrôlée des ressources système.