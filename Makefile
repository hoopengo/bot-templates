docker-build:
	docker compose up -d --build

docker-logs:
	docker logs bot-bot-1 --follow