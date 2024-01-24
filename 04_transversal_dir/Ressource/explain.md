# Explications
En Testant des chemins de fichiers standard comme "/config" "/info.php"
"/.git/config" etc... jusqu'a essayer "../" ou j ai decouvert ce message "Wtf ?"
donc j ai continuer a aller en profondeur dans le path jusqu'a "../../../../../../../etc/passwd" qui me donne le flag.

# Malveillant
Traversal Directory" ou "Path Traversal" permet à un attaquant d'accéder à des fichiers situés en dehors du répertoire racine prévu de l'application web, en exploitant les mécanismes d'inclusion de fichiers de l'application. La faille exploite cette vulnérabilité pour essayer de lire le contenu du fichier /etc/passwd du système, qui contient des informations sur les utilisateurs du système.

# Regler
Au lieu de permettre n'importe quel chemin de fichier en entrée, maintenez une liste blanche des chemins de fichier autorisés et assurez-vous que l'entrée correspond à l'un des chemins autorisés.
Au lieu de permettre n'importe quel chemin de fichier en entrée, maintenez une liste blanche des chemins de fichier autorisés et assurez-vous que l'entrée correspond à l'un des chemins autorisés.