Le modèle de sécurité d'IBM i est un cadre robuste conçu pour protéger les données, le matériel et les applications en contrôlant l'accès aux ressources au sein du système. Voici une explication détaillée des composants clés et des mécanismes de sécurité :

1. Profil Utilisateur IBM i
Un profil utilisateur est un objet qui contient des informations sur un utilisateur, telles que le nom d'utilisateur, le mot de passe, les autorisations et les paramètres de session. Il définit comment un utilisateur interagit avec le système.

Exemple : Créer un profil utilisateur avec la commande CRTUSRPRF :

CRTUSRPRF USRPRF(MARY) PASSWORD(*NEWPWD) ACTGMT(*IDENTIFY) DATFMT(*MDY) TIMFMT(*RFC)
2. Différence entre un Profil Utilisateur et un Objet
Profil Utilisateur : Contient des informations sur l'utilisateur et détermine les autorisations de cet utilisateur.
Objet : Représente une entité stockée dans le système, comme un fichier, un programme ou une bibliothèque.
3. Autorités Private et Public
Autorité Private : Contrôle l'accès à un objet pour des utilisateurs spécifiques.
Autorité Public : Détermine les autorisations accordées aux utilisateurs non spécifiés dans la liste de contrôle d’accès (ACL).
Exemple : Modifier l'autorité publique d'un fichier avec CHGATR :

CHGATR OBJ('/QRHELL/SALES') ATTR(*PUBLIC) VALUE(*EXCLUDE)
4. Rôle de QSECOFR
QSECOFR (Security Officer) est un profil système spécial utilisé par les administrateurs de sécurité pour effectuer des tâches de gestion de la sécurité qui nécessitent des privilèges élevés, comme la création et la modification de profils utilisateur, et l'accès à tous les objets du système.

5. Autorité Adoptée (Adopted Authority)
L'autorité adoptée permet à un programme d'exécuter des actions en utilisant les autorisations du profil utilisateur qui a lancé le programme, plutôt que celles du propriétaire du programme.

Exemple : Utiliser l'autorité adoptée dans un programme CL :

PROMPT('Exemple de programme avec autorité adoptée')
PGM
     SNDACTMSG MSG(QRNVUSED) TOPRC(*ALL)
ENDPGM
6. Contrôle des Droits d’un Utilisateur sur un Objet
Les droits sont contrôlés via les listes de contrôle d’accès (ACL), où chaque objet peut avoir une autorisation public et plusieurs autorisations private pour différents utilisateurs ou groupes.

Exemple : Accorder des droits en lecture à un utilisateur sur un fichier :

ADDRRT OBJ('/QRHELL/SALES') OBJTYPE(*FILE) USER(MARY) RTVAUT(*PUBLIC)
7. Bonnes Pratiques pour Sécuriser un Système IBM i
Utiliser des mots de passe forts : Obliger l'utilisation de mots de passe complexes et régulièrement renouvelés.
Limitation de session : Configurer des temps d'inactivité limités pour les sessions utilisateur.
Segmentation des autorisations : Accorder le principe du moindre privilège, en donnant uniquement les droits nécessaires.
Surveillance et audit : Activer l'audit des actions critiques et examiner régulièrement les journaux d'activité.
Mises à jour de sécurité : Appliquer régulièrement les PTF (Program Temporary Fixes) pour corriger les vulnérabilités.
Exemple concret : Activer l'audit pour un type d'événement avec AUDRRCDE :

CHGAUD AUDRRCDE(*ALLSRV) AUDLVL('SECURITY AUDIT')
En suivant ces principes et en utilisant les commandes appropriées, vous pouvez renforcer la sécurité de votre système IBM i, minimisant ainsi le risque d'accès non autorisé et de violations de données.