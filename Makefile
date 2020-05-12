help:
	@echo "install"
	@echo "   Install project dependencies."
	@echo "run"
	@echo "   Run local development server."
	@echo "lint"
	@echo "   Run project linters and autoformatters."


install:
	pip install -r requirements.txt
	
run:
	python manage.py runserver

lint:
	black .