
# =====================
# Development tasks
# =====================

# Run the dev server in the foreground
.PHONY: dev
dev: dev-image
	docker-compose -f docker-compose.yml up webdev

# Run the dev server in the background
.PHONY: up
up: dev-image
	docker-compose -f docker-compose.yml up -d webdev

# Bring down the dev server
.PHONY: down
down:
	docker-compose -f docker-compose.yml down

# Show logs from a dev server running in the background
.PHONY: logs
logs:
	docker-compose logs webdev

# Run tests
.PHONY: test
test: test-image
	docker-compose -f docker-compose.yml run test

# Test backend only
.PHONY: test-nemo
test-nemo:
	docker-compose -f docker-compose.yml run -e NEMO_TEST=nemo test

# Test frontend only
.PHONY: test-marlin
test-marlin:
	docker-compose -f docker-compose.yml run -e NEMO_TEST=marlin test

# =====================
# Lint
# =====================
.PHONY: lint-nemo
lint-nemo: dev-image
	docker-compose -f docker-compose.yml run webdev pylint nemo

.PHONY: lint-marlin
lint-marlin: dev-image
	docker-compose -f docker-compose.yml run webdev yarn run eslint "src/marlin/**"

# =====================
# Image builds
# =====================

.PHONY: image
image: base-image
	echo "Not implemented. Stop."

.PHONY: test-image
test-image: base-image tests/Dockerfile tests/requirements.txt
	docker-compose -f docker-compose.yml build test

.PHONY: dev-image
dev-image: base-image Dockerfile.dev requirements.dev.txt
	docker-compose -f docker-compose.yml build webdev

# Build the base image. All other images depend on the base image
.PHONY: base-image
base-image: Dockerfile.base requirements.txt package.json
	docker build -f Dockerfile.base  -t nemo_base:latest .
