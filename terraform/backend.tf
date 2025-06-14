terraform {
  backend "s3" {
    bucket         = "hafizwasay-todo-app-tfstate" # <<-- YOUR NEW S3 BUCKET NAME
    key            = "todo-swarm/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "hafizwasay-terraform-locks" # <<-- YOUR NEW DYNAMODB TABLE NAME
  }
}