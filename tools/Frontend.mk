init:
	yarn install

lint:
	yarn lint && yarn prettier-check && yarn type-check

jest:
	yarn test

build:
	yarn build

build-storybook:
	yarn build-storybook

test-ci:
	yarn test --coverage

deploy:
	#aws s3 rm s3://$(TARGET_S3_BUCKET) --recursive
	aws s3 sync build/ s3://$(TARGET_S3_BUCKET) --acl public-read

deploy-storybook:
	#aws s3 rm s3://$(TARGET_S3_BUCKET_STORYBOOK) --recursive
	aws s3 sync storybook-static/ s3://$(TARGET_S3_BUCKET_STORYBOOK) --acl public-read
