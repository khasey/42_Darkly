# Explications
En allant sur cette page "/index.php?page=feedback" si dans le field message on ecrit 'script' on obtien le flag 

# Malveillant
une faille XSS peut permettre de rediriger vers un site / page pour grab les cookies d'un admin ou autres utilisateurs.
Certains site malheureusement stock les datas en clair dans les cookies.

# Regler
il faut sanitize en backend ce que peut envoyer ces field cote client par exemple on peut avoir une fonction en backend de sanitize qui verifie si le message ne contient pas de balise 'script' avant de l envoyer en db pour le stocker etc...mais il y a des library qui font tres bien les travail.