Les tâches principales d’un administrateur IBM i sont cruciales pour assurer le bon fonctionnement, la sécurité et l’optimisation des performances du système. Voici les tâches essentielles ainsi qu’une procédure de diagnostic étape par étape :

1. Démarrer et arrêter proprement un système IBM i
Démarrage :

Assurez-vous que toutes les sources d'alimentation sont correctement connectées.
Accédez à l'interface de gestion du serveur (SMi ou via la console HMC dans des environnements virtuels).
Sélectionnez l’option pour démarrer le système et suivez les invites.
Arrêt :

Utilisez la commande ENDSYS pour arrêter le système. Cette commande permet de fermer tous les jobs en cours et de securiser les données avant l'arrêt.
Confirmez l’arrêt si nécessaire, en utilisant CNSSYS ou une interface similaire selon votre configuration.
2. Surveiller l’utilisation du CPU et de la mémoire
Outils : Utilisez le panneau d’administration (Navigator for i dans IBM Navigator for i) pour accéder aux rapports de performance.
Ressources : Consultez les journaux de performances (DSPPROF, WRKSYSSTS) pour obtenir des informations en temps réel sur l’utilisation du CPU et de la mémoire.
3. Identifier les jobs qui consomment beaucoup de ressources
Utilisez le tableau de bord des jobs (WRKACTJOB) pour afficher tous les jobs actifs et leurs statistiques de consommation de ressources.
Appliquez des filtres pour identifier rapidement les jobs à forte utilisation (CPU, mémoire).
4. Gérer les utilisateurs et leurs profils
Création : Utilisez la commande CREUSRPRF pour créer un nouveau profil utilisateur.
Modification : Ajustez les autorisations et les paramètres via CHGUSER.
Suppression : Révoquez l’accès en utilisant DLTUSRPRF.
5. Consulter les messages système
Accédez à la file des messages (DSPMSG) pour afficher et traiter les notifications du système.
Utilisez WRKMSG pour gérer les messages en attente, les corriger ou les supprimer.
6. Gérer les périphériques et les ressources système
Périphériques : Consultez et ajustez les configurations des périphériques via WRKDEVD.
Ressources : Utilisez WRKSBS pour gérer les sous-systèmes et WRKJOBQ pour superviser les files d’attente de travail.
7. Analyser un problème de performance ou un job bloqué
Procédure de diagnostic étape par étape :

Identification du symptôme :

Notez la durée exacte et les conditions dans lesquelles le problème se produit (temps, charge système, etc.).
Collecte des informations :

Exécutez WRKSYSSTS pour vérifier l’utilisation globale des ressources.
Utilisez DSPJOB QUSER pour inspecter le job en question et ses détails.
Analyse de la charge :

Recherchez les jobs consommateurs avec WRKACTJOB.
Vérifiez les journaux d’erreurs (DSPERRLOG) pour des indices sur les éventuelles erreurs système.
Diagnostic approfondi :

Utilisez WRKNET et WRKLNK pour vérifier les ressources réseau et les chemins de fichiers si le problème semble lié à l’accès aux données.
Exécutez des analyses de performances (ANZSRC, DSPOBJD) pour identifier des contraintes matérielles ou logicielles.
Correction :

Appliquez les ajustements nécessaires (par exemple, redimensionner les files d’attente de travail, corriger les paramètres de planification des jobs).
Redémarrez le système si nécessaire pour que les changements prennent effet.
Validation et suivi :

Surveillez le système après la mise en œuvre des correctifs.
Configurez des alertes ou des rapports de performance réguliers pour prévenir d’éventuels problèmes futurs.
En suivant ces étapes, un administrateur IBM i peut gérer efficacement les opérations du système, assurer son bon fonctionnement et résoudre rapidement les incidents qui peuvent survenir.