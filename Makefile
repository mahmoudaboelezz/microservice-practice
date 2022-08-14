install:
	pip install -r requirements.txt 
freeze:
	pip freeze > requirements.txt
format:
	black *.py mylib/*.py
lint:
	pylint --disable=R,C *.py mylib/*.py
test:
	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	docker build -t microservice_practice .
run:
	docker run -p 8080:8080 microservice_practice
deploy:
	#deploy 
all: install lint test build deploy