# Sistema para inscrições evento Fenalivre
# Desenvolvido com django

# é necessario que seja instalado os pacotes:
sudo apt-get install git
sudo apt-get install python-django
sudo apt-get install python-pip
pip install django-social-auth

# apos optenha o repositorio do github com um:
git clone https://github.com/evertonrobertoauler/fenalivre.git
cd fenalivre
python manage.py syncdb
python manage.py runserver

# e já ta rodando, no ip default http://127.0.0.1:8000/