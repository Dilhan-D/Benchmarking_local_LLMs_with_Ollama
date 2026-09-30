Utilisation de SSH et SFTP avec IBM i
1. Comment fonctionne SSH sur IBM i ?
SSH (Secure Shell) est un protocole de communication sécurisé permettant d'effectuer des connexions cryptées entre deux systèmes à travers une connexion non sécurisée, comme Internet. Sur IBM i, SSH peut être configuré pour autoriser les utilisateurs à se connecter en ligne de commande ou pour exécuter des commandes distantes de manière sécurisée.

Pour activer SSH sur un système IBM i, il est nécessaire d'installer et de configurer le serveur SSH. Cela implique généralement l'installation du PTF (Program Temporary Fix) requis pour le support de SSH et la configuration du profil utilisateur qui autorise les connexions SSH. Les commandes CL (STRSSHC pour démarrer le serveur SSH et ENDSSHC pour l'arrêter) sont utilisées pour gérer le service.

2. Comment se connecter à un IBM i depuis Linux ou Windows ?
Pour se connecter à un système IBM i à partir d'un ordinateur exécutant Linux ou Windows, vous pouvez utiliser un client SSH tel que PuTTY (pour Windows) ou l'interface de ligne de commande ssh intégrée à Linux/macOS. Voici les étapes générales :

Paramétrer le client SSH :

Entrez l'adresse IP ou le nom d'hôte de votre système IBM i.
Choisissez la méthode de connexion (par défaut, RSA).
Spécifiez le numéro de port SSH (standard : 22).
Connexion :

Indiquez le nom d'utilisateur et le mot de passe associé pour accéder au système IBM i.
3. Comment transférer un fichier vers l’IFS avec SFTP ?
SFTP (SSH File Transfer Protocol) est utilisé pour transférer des fichiers en toute sécurité entre un client et un serveur via la connexion SSH établie. Pour transférer un fichier vers le système de fichiers intégré (IFS) d'IBM i à partir d'un client Linux ou Windows :

Utilisation d’un client SFTP :
Lancez votre client SFTP (par exemple, FileZilla, WinSCP sur Windows ou sftp depuis la ligne de commande sous Linux).
Connectez-vous en utilisant les mêmes paramètres que pour SSH (hôte, port, utilisateur).
Une fois connecté, naviguez vers le répertoire IFS souhaité et transférez le fichier à partir du client vers ce répertoire.
4. Où sont généralement stockés les fichiers transférés ?
Les fichiers transférés via SFTP sur IBM i sont généralement stockés dans l'Integrated File System (IFS), qui est une structure de fichiers similaire à celle des systèmes Unix/Linux et Windows. Les chemins d’accès IFS ressemblent souvent à /QOpenSys/ pour les fichiers système ou /home/user/ pour les fichiers utilisateur.

5. Comment gérer les permissions des fichiers transférés ?
Les permissions des fichiers dans l'IFS peuvent être gérées avec la commande CHGATR (Modifier un attribut d'un objet) ou via le client SFTP en ajustant les droits d'accès appropriés lors du transfert. Par exemple, pour définir les permissions de lecture, d'écriture et d'exécution pour un fichier nommé exemple.txt, vous pouvez utiliser :

CHGATR OBJ('/QOpenSys/path/to/exemple.txt') X(*****) USRID(*OWNER)
Ajustez les caractères * selon le niveau de permission souhaité (R pour lecture, W pour écriture, X pour exécution).

6. Quelle différence entre FTP, SFTP et SCP ?
FTP (File Transfer Protocol) : Protocole non sécurisé utilisé pour transférer des fichiers sur Internet. Les données sont transmises en clair, ce qui les rend vulnérables à l'interception.
SFTP (SSH File Transfer Protocol) : Utilise le protocole SSH pour fournir un canal de transfert de fichiers sécurisé. Il chiffre toutes les données échangées entre le client et le serveur, offrant une meilleure sécurité que FTP.
SCP (Secure Copy Protocol) : Un autre moyen sécurisé de transférer des fichiers entre systèmes via SSH. Bien que similaire à SFTP, SCP est généralement utilisé pour copier des fichiers individuels plutôt que pour gérer des répertoires entiers.
7. Quels sont les principaux problèmes rencontrés lors d’un transfert de fichiers vers l’IFS ?
Problèmes de permission : S'assurer que le profil utilisateur a les droits nécessaires pour accéder et écrire dans le répertoire IFS.
Compatibilité des systèmes : Les différences entre les formats de fichiers et les conventions de nommage sur différents systèmes peuvent poser problème.
Synchronisation des fuseaux horaires : Pour les processus automatisés, il peut être nécessaire de synchroniser les fuseaux horaires pour éviter des problèmes de planification ou d'exécution.
Exemple complet de transfert de fichier entre un serveur externe et IBM i
Supposons que nous voulons transférer un fichier nommé report.pdf depuis un ordinateur Linux vers le répertoire /QOpenSys/users/home/user/Documents sur un système IBM i.

Sur le client Linux :

Ouvrez une terminal.
Utilisez la commande SFTP pour vous connecter à l'IBM i :
sftp user@ibmi_host_ip
Après connexion, utilisez la commande put pour transférer le fichier :
put report.pdf /QOpenSys/users/home/user/Documents/
Sur l'IBM i :

Une fois le transfert terminé, vous pouvez vérifier que le fichier est bien présent avec une commande CL comme DSPFFD ou simplement en listant le répertoire IFS :
WRKLNK '/QOpenSys/users/home/user/Documents'
Cet exemple illustre un transfert de fichier sécurisé et direct entre un système externe et IBM i, en utilisant SFTP pour garantir la sécurité des données.