TEST_ASSETS := $(shell for pkg in `grep -o '"\.\.\/.*"' pyproject.toml | grep -v da-pytest-fixtures |sed -e 's/"//g'`; do echo $$pkg; done)
SWEEPS := $(TEST_ASSETS:%=%/*.test)
TEST_DIR := .

.PHONY: all clean

tests: $(TEST_DIR)/*.test
CONGIF:=$(shell git rev-parse --show-toplevel)/.coveragerc
$(SWEEPS):
	cd $(@D) && poetry install && \
	poetry run pytest --cov-config=$(CONGIF) --cov=$(subst -,_,$(shell basename $(@D))) tests/


$(TEST_DIR)/%.test: $(TEST_DIR)/deps/*.test
	poetry install && poetry run pytest --cov-config=$(CONGIF) --cov=$(subst -,_,$(shell basename $(@D)))

$(TEST_DIR)/deps/%.test: $(SWEEPS)
	@echo $@ > /dev/null
