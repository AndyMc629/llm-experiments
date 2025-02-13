PROJECT_ROOT := $(PWD)
GUARDRAILS_DIR ?= $(PROJECT_ROOT)/guardrails/basic-guardrails #Allow for override of default
TRACING_DIR ?= $(PROJECT_ROOT)/tracing

install:
	poetry install

run_nemo_chat:
	@echo $(GUARDRAILS_DIR)
	@cd $(GUARDRAILS_DIR) && poetry run nemoguardrails chat

run_guardrails_example:	
	@cd $(GUARDRAILS_DIR) && poetry run python basic_guardrails.py

run_tracing_example:
	@cd $(TRACING_DIR) && poetry run python basic_tracing.py

