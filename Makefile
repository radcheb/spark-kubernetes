docker-build:
	docker-compose -f docker-compose.yaml build

shell:
	docker-compose -f docker-compose.yaml run --rm spark-master \
	  bash
