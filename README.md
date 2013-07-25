#Sistema para inscrições para o evento Fenalivre
##Desenvolvido com django

é necessaria instalação dos segintes pacotes:

	sudo apt-get install git
	sudo apt-get install python-pip
	sudo apt-get install python-virtualenv

utilize o virtualenv para que não seja necessario instalar nada específico no seu sistema operacional,
após os testes para desinstalar é so apagar a pasta DJANGO-FENALIVRE

	virtualenv DJANGO-FENALIVRE
	source DJANGO-FENALIVRE/bin/activate

instale as dependências necessarias

	pip install django
	pip install django-social-auth
	pip install django-registration

após obtenha o repositório do github e siga os demais passos:

	git clone https://github.com/evertonrobertoauler/fenalivre.git
	cd fenalivre

se você quer testar o registro normal, sem rede social, você precisa colocar um email e senha do gmail no arquivo fenalivre/settings.py, 
caso contrário não precisa, o sistema vai funcionar igual

	EMAIL_HOST_USER = 'exemplo@gmail.com'
	EMAIL_HOST_PASSWORD = 'senha'

para rodar o sistema é só dar um
 
	python manage.py syncdb
	
o syncdb vai solicitar um email e senha para usuário administrador, estes serão os seus dados para login no sistema como administrador

	python manage.py runserver
	
e já estará rodando, no endereço default: http://127.0.0.1:8000/
para desativar o virtualenv apos os testes é so dar um

	deactivate
