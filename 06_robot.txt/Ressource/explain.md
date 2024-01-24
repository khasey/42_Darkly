# Explications
En faisant une reconnaissance avec dirsearch.py 
"
[10:29:52] Starting:
[10:29:56] 200 -    1KB - /admin/?/login
[10:29:56] 200 -    1KB - /admin/
[10:29:56] 200 -    1KB - /admin/index.php
[10:30:01] 200 -  967B  - /errors/
[10:30:01] 200 -    1KB - /favicon.ico
[10:30:02] 200 -  967B  - /images/
[10:30:02] 200 -  967B  - /includes/
[10:30:02] 200 -    7KB - /index.php
[10:30:03] 200 -  967B  - /js/
[10:30:07] 200 -   53B  - /robots.txt
"
en inspectant le robots.txt 
"
    User-agent: *
    Disallow: /whatever
    Disallow: /.hidden
"
en allant voir le dossier /whatever je trouve "root:437394baff5aa33daa618be47b75cb49" 
je pense un login/pass hash md5.
je unhash avec ce site "https://www.md5online.org/md5-decrypt.html" et j obtiens "qwerty123@" et comme on le voit dans mes logs dirsearch il y a un dir "/admin/" il suffit donc juste d entrer le login/pass dans les field de la page "/admin/"

# Malveillant
Bien que robots.txt soit utilisé pour dire aux moteurs de recherche de ne pas indexer certaines pages, il ne doit pas être utilisé pour cacher des répertoires sensibles. Les attaquants peuvent consulter robots.txt pour trouver des répertoires cachés.

# Regler
proteger son dossier par un htaccess.
ou
ne pas avoir de robots.txt