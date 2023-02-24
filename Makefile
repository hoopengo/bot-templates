docker-build:
	docker compose -f docker-compose.yml up -d --build
docker-down:
	docker compose down -v
