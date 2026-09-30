IBM i : système d'exploitation hybride
IBM i est un système d’exploitation unique qui combine des fonctionnalités de gestion de données transactionnelles et de serveur d’applications dans une plateforme sécurisée.
 Conçu pour le matériel Power Systems, il intègre les technologies AS/400 (renommé iSeries) et Pervasive PDAX, offrant un environnement autonome distinct des systèmes Linux 
 ou Windows classiques.

AS/400 / IBM iSeries / Power System IBM i en 100 mots
L’AS/400, rebaptisé iSeries puis IBM i sous architecture Power Systems,
 est une plateforme serveur intégrant système d’exploitation, matériel et outils de développement. 
 Il offre un modèle de programmation basé sur des fichiers physiques et logiques, gestion centralisée des transactions et sécurité avancée, 
 tout en supportant des applications modernes via Java, SQL et interfaces REST. Conçu pour la fiabilité 24/7, il sert les secteurs finance, santé et services publics.

Principaux composants d’IBM i

OS IBM i : gestion du matériel, processus, ressources et sécurité.
DB2 for i : base de données relationnelle intégrée avec SQL.
Bibliothèques : conteneurs hiérarchiques pour programmes, journaux, objets.
Fichiers physiques/logiques : accès transparent aux données.
Interface CL (Command Language) : ligne de commande puissante.
ILE (Integrated Language Environment) : facilité de développement en C, RPG, COBOL.
Rôle de DB2 for i
DB2 for i fournit un moteur de gestion de données robuste intégré au système d’exploitation, offrant stockage sécurisé, 
transactions ACID, indexation et optimisation pour les charges lourdes. Il permet des requêtes SQL complexes, gère automatiquement 
la récupération après panne et supporte des niveaux élevés de confidentialité des données.

Bibliothèque IBM i : définition et principales bibliothèques systèmes
Une bibliothèque est un conteneur hiérarchisé regroupant objets (programmes, journaux, fichiers). Les bibliothèques systèmes clés incluent :

QSYS : contient les objets système d’origine.
QSYS2 : version à deux partitions pour compatibilité.
QTEMP : espace temporaire pour chaque travail, supprimé après son exécution.
QGPL : conteneur de gabarits et exemples fournis par IBM.
Ces bibliothèques facilitent la gestion des ressources et garantissent une isolation des données par travail.