#Sistema para inscrições para o evento Fenalivre
##Desenvolvido com django

é necessaria instalação dos segintes pacotes:

    sudo apt-get install git
    sudo apt-get install python-django
    sudo apt-get install python-pip
    pip install django-social-auth

após obtenha o repositório do github e siga os demais passos:

    git clone https://github.com/evertonrobertoauler/fenalivre.git
    cd fenalivre
    python manage.py syncdb
    python manage.py runserver

e já estará rodando, no endereço default http://127.0.0.1:8000/"