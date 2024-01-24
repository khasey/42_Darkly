# Explications
Sur la page Survey j ai repere un bug avec le form de grade que l on peut changer de 1 a 10 mais quand on le change il reste a 1 donc j ai creusé et inspecter la page et j en suis venu a changer directement la value dans "<option value="1000">1</option>" et le flag apparait 

# Malveillant
L'application ne valide pas suffisamment la valeur soumise côté serveur, permettant à un utilisateur de modifier la valeur du formulaire côté client (par exemple, en utilisant les outils de développement du navigateur) et de soumettre une valeur qui n'est pas prévue ou autorisée par l'application.

# Regler
Vérifiez toujours les données soumises côté serveur. Assurez-vous que la valeur soumise est l'une des options valides définies côté serveur.
Ne vous fiez jamais aux contrôles de l'interface utilisateur pour l'application de la logique métier ou de la logique de sécurité.
En cas de réception d'une valeur inattendue ou non autorisée, enregistrez l'incident pour une analyse ultérieure.
Affichez un message d'erreur approprié à l'utilisateur sans révéler des informations sensibles.
Utilisez des jetons anti-CSRF pour protéger les formulaires contre les attaques de type cross-site request forgery.
Limitez le taux de requêtes pour les actions sensibles pour réduire le risque d'exploitation automatisée ou de bruteforce.