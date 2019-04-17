Pour rouler les trois conteneurs Docker du projet \
`docker-compose build`
`docker-compose up`\
marche sur Ubuntu 18.04\
Sinon vous pouvez toujours rouler les dockerfile de chanque sous dossier  d'ici.\
Si vous avez une erreur d'initilisation du docker ou app ne trouve pas les tables, essayer de détruire l'image bd et repartir.\
Sa prend du temps à partir le docker de bd, vous allez possiblement avoir des erreurs de connection pour le docker de App\
Le site web se trouve sur localhost:8080 si le port est libre au démarrage\
Le REST API flask est au localhost:5000\
et la bd au localhost:3306\

Have mercy on us. Cheers!