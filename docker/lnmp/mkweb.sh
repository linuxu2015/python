#!/bin/bash
mkdir /srv/www/$1/logs -p
cp /srv/www/index.php /srv/www/$1
docker build -t $1 .
docker run -d -p 80 -v /srv/www/$1:/web --name $1 $1
docker ps -a | grep $1

