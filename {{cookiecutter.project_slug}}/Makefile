docker-run-dev:
	pipenv run python ./utils/wait_for_postgres.py
	pipenv install
	pipenv run python manage.py migrate
	#$(MAKE) seed
	#$(MAKE) parse-dev
	pipenv run python manage.py runserver 0.0.0.0:8000

lock:
	pipenv lock -r > requirements.txt

run-celery:
	celery worker -A app -l debug

run-flower:
	flower -A app

index:
	pipenv run python manage.py build_index

migrate:
	pipenv run python manage.py makemigrations
	pipenv run python manage.py migrate