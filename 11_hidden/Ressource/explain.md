# Explications
je suis revenu sur le "/.hidden" dans le "robots.txt" qui est rempli de dossier avec des README en me disant que forcement un de ces README contient le flag, en creant un script python pour crawl tous ce dossier "/.hidden" on obtien le flag.


# Malveillant
Bien que robots.txt soit utilisé pour dire aux moteurs de recherche de ne pas indexer certaines pages, il ne doit pas être utilisé pour cacher des répertoires sensibles. Les attaquants peuvent consulter robots.txt pour trouver des répertoires cachés.

# Regler
En utilisant plutot un htaccess pour proteger un dossier avec des fichiers qu'on ne veut pas montrer ou include ce dossier dans un .gitignore