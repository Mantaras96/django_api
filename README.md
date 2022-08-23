# django_api
Test api with django


Create virtual enviroment
    - python3 -m venv env

Activar el env
    - source env/bin/activate

Instalar django
    - pip install Django==3.2.4
Mirar paquetes del env
    - pip list
Crear app
django-admin startproject Proyecto_API


----------- Database -------

Crear base de datos con dcoker (mysql)
docker run --name some-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql

Crear database (SQL).
Create database djnago_api;
