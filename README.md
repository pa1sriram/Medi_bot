# Medi_bot
It is a medical bot project which helps non-technical persons obtain a brief knowledge about diseases

# STEPS

### STEP 01:Clone the repository
git clonehttps://github.com/entbappy/Build-a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS.git

### STEP 02- Create a conda environment after opening the repository
conda create -n medibot python=3.10 -y
conda activate medibot

### STEP 03- install the requirements
pip install -r requirements.txt

### Create a .env file in the root directory and add your Pinecone & OpenAI credentials as follows:
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#run the following command to store embeddings to Pinecone
python store_index.py

#Finally, run the following command
python app.py

### Now,
open up localhost:

### Techstack Used:
Python
LangChain
Flask
GPT
Pinecone

# AWS-CICD-Deployment-with-Github-Actions
###1. Log in to the AWS console.
###2. Create IAM user for deployment
#with specific access

1. EC2 access: It is a virtual machine

2. ECR: Elastic Container Registry to save your Docker image in AWS


#Description: About the deployment

1. Build a Docker image of the source code

2. Push your Docker image to ECR

3. Launch Your EC2 

4. Pull your image from ECR in EC2

5. Launch your Docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
### 3. Create an ECR repo to store/save Docker image
- Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot
### 4. Create EC2 machine (Ubuntu)
### 5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
### 6. Configure EC2 as a self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
### 7. Set up GitHub secrets:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
PINECONE_API_KEY
OPENAI_API_KEY
