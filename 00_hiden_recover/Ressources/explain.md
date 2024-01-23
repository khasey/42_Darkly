# Explications
sur cette page /index.php?page=recover on voit que l on peut
recover un mot de passe mais generalement il y a un textfield
pour mettre une adresse mail mais dans notre cas il y a rien.
En inspectant la page on peut trouver ceci ==-> "
``` 
    <input type="hidden" name="mail" maxlenght="15" value="">

```
"
en gros en changeant la value on obtien le flag.

# Malveillant
Mail bomb en utilisant un script qui passe par ce form.

# Regler
Gerer le formulaire en backend pour eviter d afficher ces params sensibles au client.

exemple: 
==> Comparez si l email soumis est bien en base de donnee avant la prochaine action.

==> Bloquez temporairement les utilisateurs qui dépassent le seuil de requêtes autorisées.

==> Envoyez un lien de récupération à l'adresse e-mail plutôt que de permettre la récupération directe ou le changement de mot de passe en ligne.