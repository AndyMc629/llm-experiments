PROJECT_ROOT := $(PWD)
GUARDRAILS_DIR ?= $(PROJECT_ROOT)/guardrails/basic-guardrails #Allow for override of default

install:
	poetry install

run_nemo_chat:
	@echo $(GUARDRAILS_DIR)
	@cd $(GUARDRAILS_DIR) && poetry run nemoguardrails chat

run_example:	
	@cd $(GUARDRAILS_DIR) && poetry run python basic_guardrails.py

