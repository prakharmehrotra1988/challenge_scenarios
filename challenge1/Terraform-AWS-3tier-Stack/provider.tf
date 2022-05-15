# Provider Configuration
terraform {
  required_providers {            #Provider is a Terraform plugin that allows users to manage an external API.
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1" 
}