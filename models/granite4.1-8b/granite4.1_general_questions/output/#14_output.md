Architecture Typique d'une Application Métier en RPGLE sur IBM i
Composants Clés et Leurs Rôles
Programmes RPGLE : Ce sont les unités de base du langage RPG (Report Program Generator) adapté pour le système IBM i. Ils contiennent la logique métier, traitent les entrées utilisateur, effectuent des calculs et gèrent l'interaction avec d'autres composants du système.

Modules : Dans le contexte de RPGLE, un module est une unité de compilation qui regroupe un ou plusieurs programmes ou fonctions compilés en un seul fichier objet. Les modules permettent de séparer la logique métier en parties réutilisables et modulaires.

Service Programs : Ce sont des collections de procédures (ou fonctions) partageant une même activation groupes, offrant ainsi une encapsulation et une réutilisation facilitées des fonctionnalités communes à plusieurs programmes. Les service programs permettent d'isoler la logique métier complexe et de l'exposer via un interface standard.

DB2 for i : Il s’agit du moteur de base de données intégré dans IBM i, offrant un accès relationnel aux données stockées. Les programmes RPGLE communiquent avec DB2 pour lire, insérer, mettre à jour et supprimer des enregistrements selon les besoins métier.

Procédures : Dans le cadre des service programs, les procédures sont les sous-programmes exposés pour être appelés par d'autres programmes ou modules. Elles définissent une logique spécifique qui peut être réutilisée à travers différentes parties de l'application.

Bibliothèques : Les bibliothèques sur IBM i regroupent des objets tels que les programmes, les données, les autorisations et autres ressources. Elles organisent les éléments d'une application de manière hiérarchisée et centralisée, facilitant l'accès et la gestion.

IFS (Integrated File System) : Il fournit un système de fichiers pour accéder aux données hors du modèle traditionnel IBM i, permettant le stockage et la récupération de fichiers texte, images, etc., au delà des bibliothèques et des journaux standard.

Jobs : Un job représente une instance d'exécution d'une application ou d'un processus sur IBM i. Chaque job contient son propre espace de travail, ses ressources et peut inclure plusieurs sous-jobs (par exemple, lorsqu'un programme appelle un autre).

Activation Groups : Elles définissent le cycle de vie des objets compilés dans un service program ou un programme principal. Les activation groups permettent le chargement conditionnel et l'initialisation en mémoire des objets au démarrage d'un job, les conservant jusqu'à ce qu'ils soient explicitement désactivés.

Objets IBM i : En général, il s’agit de toute entité manipulable sur le système IBM i (programmes, bibliothèques, journaux, autorisations, etc.). Chaque objet possède des attributs définissant son type, ses droits d'accès et sa gestion.

Flux d'une Demande Utilisateur
Voici comment une demande utilisateur peut traverser ces composants depuis l'appel initial jusqu'à la lecture ou modification de données DB2 :

Appel Initial : L'utilisateur lance l'application via un menu ISPF, une interface web (via HTTP), ou directement par un programme CL qui appelle un programme RPGLE.

Exécution du Programme Principal : Le programme RPGLE principal est chargé dans le job actif. S'il utilise des service programs, ceux-ci sont activés dans le même activation group si nécessaire pour garantir une initialisation optimale et partagée des ressources.

Utilisation de Procédures/Sous-programmes : Le programme principal appelle des procédures d'un service program pour traiter des tâches spécifiques (par exemple, validation de données).

Interaction avec DB2 for i : Pour lire ou modifier les données, le programme RPGLE utilise des instructions SQL intégrées à l'interprétation RPGLE (ou via des interfaces JDBC/ODBC). Les requêtes sont envoyées directement à DB2 pour traitement.

Accès aux Données : Si nécessaire, le programme peut également accéder au système de fichiers IFS pour lire ou écrire des fichiers non relationnels.

Gestion des Ressources : Toute la logique est gérée dans le contexte d'un job IBM i, avec les objets (programmes, modules) vivant dans leurs bibliothèques respectives et pouvant être partagés via l'activation groupes pour optimiser l'utilisation de la mémoire.

Terminaison du Job : Une fois le traitement terminé, le job se termine, libérant les ressources allouées (sauvegarde des données en cours d'utilisation dans le système journaux, etc.), et le résultat final est présenté à l'utilisateur.

Ce parcours illustre comment une demande utilisateur déclenche une séquence complexe de processus sur IBM i, intégrant logique métier, base de données, gestion des fichiers et ressources système, tout en exploitant la robustesse et l'efficacité du modèle d'exécution RPGLE.