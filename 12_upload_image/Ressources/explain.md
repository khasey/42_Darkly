# Explications
avec mon experience dans le hack je sais que la facon la plus facile d avoir un reverse shell est la page d upload, en gros il faut reussir a upload un fichier php en contournant les securite du module form upload si il y en a.
dans notre cas on voit que je ne peux pas upload directement un fichier avec l extension .php mais on peut upload un fichier avec une extension en plus comme par exemple "a.php.jpeg" dans ce cas la le site accepte l upload et nous prompt cette string 
"/tmp/a.php.jpeg succesfully uploaded."
Si l'application a des paramètres qui acceptent des chemins de fichiers (par exemple, ?page=..), on peut essayer d'exploiter une vulnérabilité de type LFI (Local File Inclusion) en incluant le chemin de notre fichier téléchargé comme paramètre.
Donc je test d aller sur la page donné "http://tonIP/?page=/tmp/a.php.jpeg" et cette page m envoit une alert "WTF?" cest qui me confirme qu il y a une faille ici mais la methode n est pas bonne.

La bonne methode est d utiliser cURL pour faire une requete POST en changeant le type MIME donc en faisant croire au form upload que le fichier est bien un .jpeg voici la CMD 
```
curl -s -X POST -F "uploaded=@/lePathDeVotreFichierPHP;type=image/jpeg" -F "Upload=Upload" "http://votreIP/index.php?page=upload" | grep 'flag'
```
ce qui nous donne le flag



# Malveillant
La page d'upload de fichiers ne valide pas suffisamment le type de fichier téléchargé, permettant le téléchargement de fichiers autres que des images, y compris des scripts exécutables comme des fichiers PHP.
Si le serveur web est configuré pour exécuter des fichiers PHP dans le répertoire où les fichiers sont téléchargés, et si le fichier téléchargé est accessible via une URL, un attaquant pourrait exécuter le script PHP en accédant à son URL, conduisant potentiellement à l'exécution de code arbitraire sur le serveur.

# Regler

Vérifiez l'extension et le type MIME du fichier, mais ne vous y fiez pas uniquement. Vérifiez également le contenu du fichier pour vous assurer qu'il correspond au type de fichier attendu.
Stockez les fichiers téléchargés dans un répertoire qui n'exécute pas les scripts. Configurez correctement le serveur web pour ne pas exécuter de fichiers dans les répertoires de téléchargement.
Renommez les fichiers téléchargés avec un nom généré par le serveur pour éviter toute exécution directe de scripts.

