all:
	make docker-compose
	make run
	make check

docker-compose:
	docker compose up -d

run:
	poetry run python docker_minio_error_reproduction

check:
	docker ps