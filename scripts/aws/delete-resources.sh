# aws cloudformation delete-stack --stack-name KozmoaiAppStack
aws ecr delete-repository --repository-name kozmoai-backend-repository --force
# aws ecr delete-repository --repository-name kozmoai-frontend-repository --force
# aws ecr describe-repositories --output json | jq -re ".repositories[].repositoryName"