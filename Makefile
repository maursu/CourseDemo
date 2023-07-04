make run:
	python manage.py runserver --settings=config.settings.local

make admin:
	python manage.py createsuperuser

make migrate:
	python manage.py makemigrations
	python manage.py migrate

make static:
	python manage.py collectstatic

make test:
	python manage.py test

make shell:
	python manage.py shell

make docker-admin:
	docker-compose exec -it main_api python manage.py createsuperuser

#  gunicorn --bind 0.0.0.0:8000 config.wsgi:application"
