_all: all container
_clean: clean clean_container

include ../../../tools/Packages.mk
include ../../../tools/Containers.mk
include ../../../tools/Terraform.mk
include ../../../tools/Testing.mk


BOLD=$(shell tput bold)
RED=$(shell tput setaf 1)
GREEN=$(shell tput setaf 2)
YELLOW=$(shell tput setaf 3)
RESET=$(shell tput sgr0)
DIR_NAME=$(notdir $(CURDIR))
PROJECT=seedlist-server
ENV ?=stage
REGION ?=us-east-1
HOST_PREFIX ?=stage
FRONTEND_BUCKET ?=dashboard-ui-bucket
S3_BUCKET ?=$(PROJECT)-terraform-states
STATE_KEY ?=$(ENV)_$(PROJECT)_terraform.tfstate
DYNAMODB_TABLE ?=$(PROJECT)-tfstate-lock-table
WORKSPACE ?="$(ENV)-$(REGION)-$(PROJECT)-eks"
AWS_DEFAULT_REGION = $(REGION)
AWS_PROFILE ?= default
AWS_ACCESS_KEY_ID ?= $(shell aws configure get aws_access_key_id --profile $(AWS_PROFILE))
AWS_SECRET_ACCESS_KEY ?= $(shell aws configure get aws_secret_access_key --profile $(AWS_PROFILE))
AWS=AWS_ACCESS_KEY_ID=$(AWS_ACCESS_KEY_ID) AWS_SECRET_ACCESS_KEY=$(AWS_SECRET_ACCESS_KEY) AWS_DEFAULT_REGION=$(AWS_DEFAULT_REGION) aws
TERRAFORM_DIR_SUFFIX ?= ecs
TERRAFORM_DIR ?= $(shell git rev-parse --show-toplevel)/terraform/$(TERRAFORM_DIR_SUFFIX)
VERSION ?= $(shell git rev-parse HEAD )

showenv: ## Show Environment Details
	@echo 'Environment:'
	@echo '-----------------------'
	@echo 'SRC_PATH:' $(DIR_NAME)
	@echo 'PROJECT:' $(PROJECT)
	@echo 'ENVIRONMENT:' $(ENV)
	@echo 'REGION:' $(REGION)
	@echo 'S3_BUCKET:' $(S3_BUCKET)
	@echo 'STATE_KEY:' $(STATE_KEY)
	@echo 'DYNAMODB_TABLE:' $(DYNAMODB_TABLE)
	@echo 'AWS_DEFAULT_REGION:' $(AWS_DEFAULT_REGION)
	@echo 'AWS_PROFILE:' $(AWS_PROFILE)
	@echo 'DOCKER_REPO:'$(DOCKER_REPO)
	@echo 'TERRAFORM_DIR:'$(TERRAFORM_DIR)
	@echo  'DYNAMODB_TABLE:'$(DYNAMODB_TABLE)
	
