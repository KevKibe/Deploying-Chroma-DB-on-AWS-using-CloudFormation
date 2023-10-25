# Deploying-Chroma-DB-on-AWS-using-CloudFormation
- This project provides steps on how to deploy ChromaDB on AWS CloudFormation using a template.
- The template creates a stack that runs Chroma on a single EC2 instance. 
- ChromaDB is a distributed document database that is optimized for search and analytics. It is a good choice for storing and querying large volumes of text data and embeddings for access to LLMs.

## Prerequisites:
- An AWS account
- The AWS CLI
- Permissions to AWS CloudFormation through AWS CLI

## Steps
- Key in your AWS CLI credentials using the command
```
AWS configure
```
- To launch the template using CloudFormation run this command. Replace `--stack-name my-chroma-stack` with a different stack name, if you wish.
```
aws cloudformation create-stack --stack-name my-chroma-stack --template-url https://s3.amazonaws.com/public.trychroma.com/cloudformation/latest/chroma.cf.json
```
- You can customize the instance type(default is `t3.small`), and the EC2 instance to use a KeyPair to allow SSH into it using [these](https://docs.trychroma.com/deployment) instructions.
- You can find the public IP of the stack on the AWS console or run this command(make sure to use the stack name used).
```

aws cloudformation describe-stacks --stack-name my-chroma-stack --query 'Stacks[0].Outputs'
```
- Your stack is running on that IP address on port 8000 and you can add collections using this [example](https://github.com/KevKibe/Deploying-Chroma-DB-on-AWS-using-CloudFormation/blob/main/client.py) and query using this [example](https://github.com/KevKibe/Deploying-Chroma-DB-on-AWS-using-CloudFormation/blob/main/query.py).

## Additional Information
-This [notebook](https://github.com/KevKibe/Deploying-Chroma-DB-on-AWS-using-CloudFormation/blob/main/Semantic_Search_with_Chroma_DB.ipynb) is a quick tutorial to ChromaDB, specifically adding and querying collections on it.
