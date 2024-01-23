# Explications
par chance j ai trouve que dans le footer les redirections social pouvaient etre change
exemple:
``` 
    <a class="icon fa-facebook" href="index.php?page=redirect&site=https://www.google.com/">

```
"
changer le href nous donne le flag.

# Malveillant
on peut utiliser cette faille pour faire du phishing.

# Regler
Creer une liste blanche des URLs
N'autorisez les redirections qu'à une liste prédéfinie d'URLs de confiance. Cela peut être réalisé en vérifiant l'URL de destination contre une liste blanche d'URLs autorisées.

```
    <?php
$allowedUrls = [
    'https://facebook.com/yourpage',
    'https://twitter.com/yourpage',
];

$url = $_GET['redirectUrl'] ?? '';

if (in_array($url, $allowedUrls)) {
    header("Location: $url");
} else {
    die('Redirection non autorisée.');
}
?>

```