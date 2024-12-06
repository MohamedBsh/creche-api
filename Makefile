PYTHON=python3
FLAKE8=flake8
BLACK=black
TEST_DIR=creche/tests
SRC_DIR=creche

.PHONY: all
all: lint test

.PHONY: test
test:
	@echo "Running unit tests..."
	$(PYTHON) -m unittest discover -s $(TEST_DIR)

.PHONY: lint
lint:
	@echo "Checking code style with flake8..."
	$(FLAKE8) $(SRC_DIR)

.PHONY: format
format:
	@echo "Formatting code with black..."
	$(BLACK) $(SRC_DIR)

.PHONY: clean
clean:
	@echo "Cleaning temporary files..."
	find . -type d -name '__pycache__' -exec rm -r {} +