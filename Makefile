SHELL := /bin/bash

setup:
	docker run --name fastapi_udon_db \
	-e POSTGRES_USER=postgres \
	-e POSTGRES_PASSWORD=root \
	-e POSTGRES_DB=fastapi_udon_db \
	-p 5432:5432 \
	-d postgres && \
	oban install

dev:
	fastapi dev --reload & oban start