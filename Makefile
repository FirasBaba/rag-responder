file_dir ?= $(realpath .)
build:
	docker-compose build

run:
	docker run \
	-v "${file_dir}/data":/data \
	-v "${file_dir}/src":/src \
	-ti rag-responder \
	/bin/bash

jupyter:
	docker run \
	-v "${file_dir}/data":/data \
	-v "${file_dir}/src":/src \
	-p 8888:8888 \
	-ti rag-responder \
	jupyter lab --ip=0.0.0.0 --no-browser --allow-root

run-ollama:
	docker-compose run \
	-e OLLAMA_MODEL_NAME="${OLLAMA_MODEL_NAME}" \
	ollama-service

run-chat:
	docker-compose run \
	-e OLLAMA_MODEL_NAME="${OLLAMA_MODEL_NAME}" \
	rag-responder \
	python3 main.py

run-reader:
	docker-compose run \
	rag-responder \
	python3 create_book_db.py