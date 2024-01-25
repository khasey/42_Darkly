# Explications
Sur la page home j ai etudié la seul photo qui a une redirection 
```<a href="?page=media&src=nsa">```
Un attaquant peut fournir une chaîne malveillante en tant que valeur de src. Dans le code actuel on peut remplace la string par "data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4=" une chaîne en base64 qui décode vers <script>alert(1);</script>, un script JavaScript qui déclenche une alerte.


# Malveillant
Cross-Site Scripting (XSS) qui est exploitable via un paramètre de requête utilisé dans un "viewer" d'image. Cette vulnérabilité se manifeste lorsque l'application insère de manière non sécurisée le contenu d'une entrée utilisateur (dans ce cas, le paramètre src) directement dans le HTML, permettant l'exécution de scripts arbitraires.

# Regler
Assurez-vous de valider et d'échapper toutes les entrées utilisateur, en particulier celles qui sont insérées directement dans le HTML. Utilisez des bibliothèques et des fonctions spécifiques pour échapper les entrées pour le contexte dans lequel elles seront utilisées (HTML, URL, JavaScript, etc.).
Mettez en place des Politiques de Sécurité du Contenu (Content Security Policy - CSP) pour limiter les sources à partir desquelles le contenu (scripts, images, etc.) peut être chargé. Cela peut aider à atténuer l'impact des attaques XSS.