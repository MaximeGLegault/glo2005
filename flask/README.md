Créer le docker \
`docker run -d --name some-mysql -p 6033:3306 -e MYSQL_ROOT_PASSWORD=1234 mysql --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci`

Stopper le docker \
`docker stop some-mysql`

Restarter le docker \
`docker start some-mysql`

Passer un script .sql au docker pour initialiser la base de données\
`docker exec -i some-mysql mysql < scripts/db_init.sql  `

Acceder à la bd dans docker \
`docker exec -it some-mysql mysql -p1234`