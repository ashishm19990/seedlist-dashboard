.PHONY: prep tf_format tf_apply tf_apply tf_apply_auto_approve tf_destroy

prep:  ## Prepare a new workspace (environment) if needed, configure the tfstate backend, update any modules, and switch to the workspace
	@echo "Verifying that the S3 bucket $(S3_BUCKET) for remote state exists."
	@if ! aws --profile $(AWS_PROFILE) s3api head-bucket --region $(REGION) --bucket $(S3_BUCKET) ; then \
		echo $(FAIL)"[ERROR] S3 bucket $(S3_BUCKET) was not found, creating new bucket with versioning enabled to store tfstate"$(END);\
		aws --profile $(AWS_PROFILE) s3api create-bucket --bucket=$(S3_BUCKET) --region=$(REGION)   --acl=private; \
		aws --profile $(AWS_PROFILE) s3api put-bucket-versioning --bucket $(S3_BUCKET) --versioning-configuration Status=Enabled ; \
		aws --profile $(AWS_PROFILE) s3api put-public-access-block --bucket $(S3_BUCKET) --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"; \
		echo "$(BOLD)$(GREEN)S3 bucket $(S3_BUCKET) created$(RESET)"; \
	else \
		echo "$(BOLD)$(GREEN)S3 bucket $(S3_BUCKET) exists$(RESET)";\
	fi

	@echo "$(BOLD)Verifying that the DynamoDB table exists for remote state locking$(RESET)"
	@if ! aws --profile $(AWS_PROFILE) --region $(REGION) dynamodb describe-table --table-name $(DYNAMODB_TABLE) ; then \
		echo "$(BOLD)DynamoDB table $(DYNAMODB_TABLE) was not found, creating new DynamoDB table to maintain locks$(RESET)"; \
		aws --profile $(AWS_PROFILE) dynamodb create-table \
			--region $(REGION) \
			--table-name $(DYNAMODB_TABLE) \
			--attribute-definitions AttributeName=LockID,AttributeType=S \
			--key-schema AttributeName=LockID,KeyType=HASH \
			--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 > /dev/null 2>&1 ; \
		echo "$(BOLD)$(GREEN)DynamoDB table $(DYNAMODB_TABLE) created$(RESET)"; \
		echo "Sleeping for 10 seconds to allow DynamoDB state to propagate through AWS"; \
		sleep 10; \
	else \
		echo "$(BOLD)$(GREEN)DynamoDB Table $(DYNAMODB_TABLE) exists$(RESET)"; \
	fi
	@echo "$(BOLD)Configuring the terraform backend$(RESET)"
	@terraform -chdir=$(TERRAFORM_DIR) init\
		-backend=true\
		-backend-config="profile=$(AWS_PROFILE)"\
		-backend-config="region=$(REGION)"\
		-backend-config="bucket=$(S3_BUCKET)"\
		-backend-config="key=$(STATE_KEY)" \
		-backend-config="dynamodb_table=$(DYNAMODB_TABLE)"\
		-backend-config="acl=private"
	@echo "$(BOLD)Switching to workspace $(WORKSPACE)$(RESET)"
	@terraform workspace select $(WORKSPACE) || terraform workspace new $(WORKSPACE)

tf_plan: prep ## Show what terraform thinks it will do
	@terraform -chdir=$(TERRAFORM_DIR) plan \
		-lock=false \
		-input=false \
		-refresh=true

tf_apply: prep ## Have terraform do the things. This will cost money.
	@terraform -chdir=$(TERRAFORM_DIR) apply \
		-lock=true \
		-input=false \
		-refresh=true \


tf_apply_auto_approve: prep ## Have terraform do the things. This will cost money.
	@terraform -chdir=$(TERRAFORM_DIR) apply -auto-approve=true \
		-lock=true \
		-input=false \
		-refresh=true


tf_destroy:  prep ## Destroy the things
	@terraform -chdir=$(TERRAFORM_DIR)  destroy -auto-approve=true\
		-lock=false \
		-input=false \
		-refresh=true \
	

tf_format:  ## Rewrites all Terraform configuration files to a canonical format.
	@terraform -chdir=$(TERRAFORM_DIR) fmt  -recursive
