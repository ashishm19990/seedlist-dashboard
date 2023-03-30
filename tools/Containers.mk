.PHONY: container clean_container docker_push docker-repo-login

# Use ./dist as build context to avoid .venv and other files from creating a fat build context
# Docker builds only install from artifacts in ./dist. We can avoid .dockerignore by adjusting
# the build context.
container:
	docker build -t $(DOCKER_REPO)/$(ENV)-cloud-genie-repo:latest -t $(DOCKER_REPO)/$(ENV)-cloud-genie-repo:$(VERSION) .

clean_container:
	-docker rmi -f $(ENV)-cloud-genie-repo:latest

# Docker publish
docker_push: aws-docker-repo-login ## Publish the `{version}` and `latest` tagged containers to ECR
	docker push $(DOCKER_REPO)/$(ENV)-cloud-genie-repo:latest
	docker push $(DOCKER_REPO)/$(ENV)-cloud-genie-repo:$(VERSION)

# generate script to login to aws docker repo
CMD_REPO_LOGIN := "eval $$\( aws ecr"
ifdef AWS_PROFILE
CMD_REPO_LOGIN += " --profile $(AWS_PROFILE)"
endif
ifdef AWS_DEFAULT_REGION
CMD_REPO_LOGIN += " --region $(AWS_DEFAULT_REGION)"
endif
CMD_REPO_LOGIN += " get-login --no-include-email \)"

# login to AWS-ECR
CMD_REPOLOGIN := "eval $$\( aws "
ifdef AWS_PROFILE
CMD_REPOLOGIN += " --profile $(AWS_PROFILE)"
endif
ifdef REGION
CMD_REPOLOGIN += " --region $(REGION)"
endif
CMD_REPOLOGIN += " ecr get-login --no-include-email \)"

aws-docker-repo-login: ## Auto login to AWS-ECR using aws-cli
	@echo 'Performing repo login into $(DOCKER_REPO)'
	aws --profile=default --region us-east-1 ecr get-login-password | docker login \
    --username AWS \
    --password-stdin $(DOCKER_REPO)
	@echo 'Completed repo login into $(DOCKER_REPO)'
