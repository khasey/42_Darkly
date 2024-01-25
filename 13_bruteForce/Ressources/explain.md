# Explications
Pendant mes injection sql j ai pu voir une table "Member Brute Force", je pense que j aurais pu directement trouver le login/pass dans ce dir mais le bruteforce est plus interessant.
en lancant le script bruteF.sh on option le flag

# Malveillant
Une faille de type "brute force" (ou force brute) est une méthode d'attaque utilisée pour obtenir des informations telles que des identifiants d'utilisateur ou des mots de passe. Dans cette approche, l'attaquant essaie systématiquement toutes les combinaisons possibles de caractères jusqu'à ce qu'il trouve la combinaison correcte. 

# Regler
Mettez en place des limites sur le nombre de tentatives de connexion autorisées sur une période donnée. Après avoir dépassé cette limite, bloquez temporairement l'accès ou exigez une action supplémentaire (comme une vérification CAPTCHA).
Verrouillez les comptes après un certain nombre de tentatives de connexion infructueuses. Informez l'utilisateur et exigez une action pour réactiver le compte (comme contacter le support ou changer de mot de passe).
Encouragez ou imposez l'utilisation de mots de passe forts (longs, avec une combinaison de lettres, de chiffres et de caractères spéciaux) pour rendre les attaques par force brute pratiquement infaisables.
Mettez en place des systèmes de surveillance pour détecter des modèles d'accès suspects et alertez les administrateurs ou les utilisateurs concernés en cas d'activité inhabituelle.
