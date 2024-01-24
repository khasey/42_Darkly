# Explications
Quand on regard les En-tetes des requete en inspectant la page on voit que le cookie est bizarre "Cookie: I_am_admin=68934a3e9455fa72420237eb05902327".
en testant de unhash en md5 on obtiens "false"
--> utiliser ce site "https://10015.io/tools/md5-encrypt-decrypt" pour encrypter la valeur "true" en md5 et remplacer le hash par celui qui est a true en inspectant la page et aller dans stockage (firefox) pour remplacer le cookie puis rafraichir la page d acceuil.

# Malveillant
contrôle d'accès insuffisant où l'application dépend de la valeur d'un cookie (I_am_admin) pour déterminer si un utilisateur est administrateur ou non. L'utilisation d'un cookie facilement modifiable et d'un hachage faible comme MD5 pour une valeur de contrôle critique est une mauvaise pratique en matière de sécurité.

# Regler
Ne basez jamais la logique de sécurité ou d'authentification sur des valeurs stockées côté client.
Utilisez des identifiants de session générés côté serveur pour suivre les sessions utilisateur. Stockez les rôles et les permissions des utilisateurs côté serveur, pas dans des cookies.
