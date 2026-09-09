Utilisation des modules et des programmes de services dans une application IBM i moderne
Pourquoi séparer un programme en plusieurs modules ?
Séparer un programme en plusieurs modules offre plusieurs avantages :

Réutilisabilité : Les modules peuvent être réutilisés par différents programmes, réduisant ainsi la duplication du code.
Maintenabilité : Chaque module peut être développé et maintenu indépendamment, facilitant les modifications et les mises à jour.
Compilations rapides : Seuls les modules modifiés nécessitent une recompilation, accélérant le cycle de développement.
Clarté : Un programme contenant plusieurs modules est plus facilement compris et organisé par rapport à un grand programme unique.
Quelle différence entre compiler un module et créer un programme ?
Compiler un module (CRTRPGMOD ou équivalent) produit un fichier de module compilé (.NCC), qui contient le code mais n'est pas encore un programme exécutable.
Créer un programme (CRTPGM ou équivalent) assemble les modules (et éventuellement des programmes existants) en un seul objet PGM exécutable.
Quel est le rôle de CRTRPGMOD, CRTSRVPGM et CRTPGM ?
CRTRPGMOD : Compile un programme RPG en un module compilé.
CRTSRVPGM : Crée un programme de services à partir d'un ou plusieurs modules, exposant les procédures (procedures) qu'il contient pour une utilisation par d'autres programmes.
CRTPGM : Assemble des modules en un programme exécutable final. Peut également être utilisé pour créer des programmes de services si les modules sont déjà regroupés dans un CRTSRVPGM.
Qu'est-ce qu'une procédure exportée ?
Une procédure exportée est une fonction ou un sous-programme défini dans un programme de services qui peut être appelée depuis d'autres programmes. Elle est exposée à l'extérieur du programme de services pour permettre cette réutilisation.

Comment une procédure est-elle importée par un autre programme ?
Une procédure exportée d'un programme de services est importée dans un autre programme en spécifiant le nom du service program et la procédure souhaitée dans l'en-tête du programme source (par exemple, via MODULE(*SRVPGM) ou des directives spécifiques au langage). Le compilateur s'occupera de lier cette procédure pendant la compilation.

Pourquoi utiliser un service program plutôt qu'un simple programme ?
Isolation : Les programmes de services isolent le code logique, facilitant les mises à jour sans affecter directement les appels.
Réutilisation : Permet une réutilisation facile du code entre différents programmes et applications.
Maintenance : Simplifie la maintenance en centralisant le code partagé.
Comment gérer l'évolution d'un service program sans casser les applications existantes ?
Pour éviter de casser les applications existantes lors de l'évolution d'un programme de services :

Préserver la signature des procédures : Maintenir les paramètres et le type de retour des exportations.
Versioning : Utiliser des versions du programme de services (par exemple, mySrvPgm_V2) pour permettre aux applications d'attendre une version spécifique sans être affectées par les mises à jour ultérieures.
Documentation et tests : Fournir une documentation claire sur les changements et effectuer des tests rigoureux pour s'assurer que les nouvelles versions ne compromettent pas le comportement existant.
Ces pratiques garantissent la stabilité et l'évolutivité des applications IBM i modernes.