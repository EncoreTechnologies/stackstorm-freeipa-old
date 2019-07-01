THIS_FILE := $(lastword $(MAKEFILE_LIST))
ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VIRTUALENV_DIR ?= $(ROOT_DIR)/virtualenv
GIT_DIR ?= $(ROOT_DIR)/freeipa

.PHONY: all
all: fetch-spec generate

.PHONY: fetch-spec
fetch-spec: requirements .fetch-spec

.PHONY: generate
generate: requirements .generate

.PHONY: clean
clean: .clean

# list all makefile targets
.PHONY: list
list:
	@if [ -d "$(CI_REPO_PATH)" ]; then \
		$(MAKE) --no-print-directory -f $(ROOT_DIR)/ci/Makefile list; \
	fi;
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | sort | uniq | xargs


.PHONY: requirements
requirements: virtualenv
	@echo
	@echo "==================== requirements ===================="
	@echo
	. $(VIRTUALENV_DIR)/bin/activate; \
	$(VIRTUALENV_DIR)/bin/pip install --cache-dir $(HOME)/.pip-cache --upgrade pip; \
	$(VIRTUALENV_DIR)/bin/pip install --cache-dir $(HOME)/.pip-cache -q -r $(ROOT_DIR)/requirements.txt;


.PHONY: virtualenv
virtualenv: $(VIRTUALENV_DIR)/bin/activate
$(VIRTUALENV_DIR)/bin/activate:
	@echo
	@echo "==================== virtualenv ===================="
	@echo
	if [ ! -d "$(VIRTUALENV_DIR)" ]; then \
		virtualenv --no-site-packages $(VIRTUALENV_DIR);\
	fi;


.PHONY: .clean
.clean:
	@echo
	@echo "==================== clean ===================="
	@echo
	rm -rf $(VIRTUALENV_DIR)
	rm -rf $(GIT_DIR)


.PHONY: .fetch-spec
.fetch-spec:
	@echo
	@echo "==================== fetch-spec ===================="
	@echo
	. $(VIRTUALENV_DIR)/bin/activate; \
	$(ROOT_DIR)/generate_actions.py fetch-spec


.PHONY: .generate
.generate:
	@echo
	@echo "==================== generate ===================="
	@echo
	. $(VIRTUALENV_DIR)/bin/activate; \
	$(ROOT_DIR)/generate_actions.py generate
