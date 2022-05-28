
$ docker rm -vf $(docker ps -aq)

$ docker rmi -f $(docker images -aq) 

$ yes | docker image prune --all 

$ docker image prune --all --force

$ yes | docker system prune -a

$ yes | docker container prune

$ yes | docker image prune 

$ docker images 

$ docker ps -a

$ cd /mnt/d/

$ mkdir reto_dd360

$ mkvirtualenv --python=/usr/bin/python3 reto_dd360

$ cd reto_dd360

$ touch app.py

$ nano app.py

# escribir nuestro codigo python

$ touch requirements.txt	

$ nano requirements.txt

# escribir nuestros requerimientos

$ pip install -r requirements.txt

$ touch Dockerfile

$ nano Dockerfile

# escribir nuestro Dockerfile

$ docker image build -t reto_dd360:latest .

$ docker run reto_dd360:latest

$ touch docker-compose.yml

$ nano docker-compose.yml

# escribir el archivo docker-compose.yml

$ docker-compose up --build -d

$ docker ps --format '{{.Names}}' --filter="ancestor=reto_dd360_python:latest"

$ docker exec -i -t $(docker ps --format '{{.Names}}' --filter="ancestor=reto_dd360_python:latest") bash

# salir del container de docker sin apagar
"Ctrl + p" luego "Ctrl + q"

# salir del container de docker sin apagar
exit

$ crontab -l

$ service cron status

$ crontab -e

$ git init 
$ git add .
$ git commit -m "first commit"
$ git branch -M main
$ git remote add origin https://github.com/jamirhuamancampos/reto_dd360.git
$ git push -u origin main