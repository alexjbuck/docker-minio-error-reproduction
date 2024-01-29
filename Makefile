run:
	docker-compose up -d
	poetry run python docker_minio_error_reproduction
	docker ps