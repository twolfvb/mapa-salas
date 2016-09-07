# iteracion-00
# Creación de Proyectos Ágiles
Cloud9, Heroku y Travis en Django 

## Setup del Repositorio
1. Crear repositorio vacío en GitHub
2. Clonar repositorio en c9 (elegir django)
3. $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile my_app
4. Cut and paste the files from the bottom my_app directory into the top my_app directory and then delete the empty bottom directory
5. $ sudo pip install -r requirements.txt
6. $ git push origin master

## Setup de Heroku

1. $ wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
2. $ heroku login
3. P royecto nuevo en Heroku 
4. Conectarlo a GitHub (en tab “Deploy”)
5. Correr un deploy manual (heroku config:set DISABLE_COLLECTSTATIC=1)
6. Añadir remote de heroku al repositorio local a heroku git:remote -a falling-wind-1624 (reemplazar con nombre de app en heroku)
7. $ heroku run python manage.py migrate
8. $ heroku run python manage.py createsuperuser

## Setup de git-flow

1. $ sudo apt-get install git-flow
2. $ git flow init (enters)
3. Modelo: http://nvie.com/posts/a-successful-git-branching-model/
4. Cheatsheet: http://danielkummer.github.io/git-flow-cheatsheet/

## Setup de Travis

* Agregar archivo de configuracion de TravisCI https://raw.githubusercontent.com/dxc/ChileAyuda-API/master/.travis.yml
* Archivo Travis RAW:
```python
language: python
python:
  - "2.7"
# before_install:
#   - export PIP_USE_MIRRORS=true
install:
  - pip install -r requirements.txt
before_script:
  - python manage.py migrate --no-input
script:
  - python manage.py test
```
* Agregar TravisCI como servicio en repo de github

## Otros

* Coveralls (Test Coverage)
* Codeclimate
* Issues en github y cerrarlos con commits (https://wiredcraft.com/blog/how-we-write-our-github-issues/)
* Milestones
* TDD

## Fuentes: 
http://matthewstibbard.com/2016/01/15/how-to-deploy-a-django-project-in-cloud9-to-heroku/

