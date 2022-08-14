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
	aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 113415630473.dkr.ecr.eu-west-2.amazonaws.com 
	docker build -t microservice-wiki .
	docker tag microservice-wiki:latest 113415630473.dkr.ecr.eu-west-2.amazonaws.com/microservice-wiki:latest
	docker push 113415630473.dkr.ecr.eu-west-2.amazonaws.com/microservice-wiki:latest

all: install lint test build deploy