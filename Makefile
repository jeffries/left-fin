
# =====================
# Development tasks
# =====================

# Run the dev server in the foreground
.PHONY: dev
dev: dev_image
	docker-compose -f docker-compose.yml up webdev

# Run the dev server
.PHONY: up
up: dev_image
	docker-compose -f docker-compose.yml up -d webdev

# Bring down the dev server
.PHONY: down
down:
	docker-compose -f docker-compose.yml down

.PHONY: logs
logs:
	docker-compose logs webdev

# Run tests
.PHONY: test
test: test_image
	docker-compose -f docker-compose.yml run test

# =====================
# Image builds
# =====================

.PHONY: build
image: base_image
	echo "Not implemented. Stop."

.PHONY: test_image
test_image: base_image tests/Dockerfile tests/requirements.txt
	docker-compose -f docker-compose.yml build test

.PHONY: dev_image
dev_image: base_image Dockerfile.dev requirements.dev.txt
	docker-compose -f docker-compose.yml build webdev

# Build the base image. All other images depend on the base image
.PHONY: base_image
base_image: Dockerfile.base requirements.txt package.json
	docker build -f Dockerfile.base  -t nemo_base:latest .
