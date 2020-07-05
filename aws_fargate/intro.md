# AWS Fargate

Run containarized app serverless way without managing EC2 instances or servers, with no setting rules for autoscaling.

Fargate is a service for managing and deploying containers without provisioning or mantaining server (EC2) clusters to meet application needs or worrying about software updates and patching.

Fargate supports:

- ECS
- EKS

Only pay for resources used (CPU and Memory based).

Define: Memory, CPU, Image, etc.

## Running Task on Fargate

Only have to manage task and ECS Scheduling & Orchestration nor ECS Agent, Docker Agent, or ECS AMI, Cluster Manager, Placement Engine.

## Using Fargate

Can use it through AWS Console, AWS CLI, AWS ECS CLI

## Sample task definition

It launch a container image based on nginx into my environment.

```JSON
{
    "memory": 1024,
    "networkMode": "AWSVPC",
    "compatibilities": ["EC2", "FARGATE"],
    "placementConstraints": [],
    "cpu": 512,

    "containerDefinitions":[
        {
            "name": "nginx",
            "image": "nginx:latest",
            "memoryReservation": "256"
        }
    ]
}
```

## Networking in Fargate

VPC: All task launched using fargate will run within the VPC defined. As the user, we defined the subnets, security groups, etc.

Load Balancing: Application Load Balancing (ALB) and Network Load Balancing (NLB). Elastic Load Balancing is NOT supported.

## Security in Fargate

- Customer owns and manages tasks and AWS owns infrastructure.
- No SSH access to the infrastructure (Removes posibility of remote connection)
- Cluster-level isolation for containers.

## Fargate Use cases

- Long running services.
- Highly available applications.
- Monolithic app portability.
- Microservices, Batch jobs (Machine Learning Applications).

## EC2 use cases

- WIndows Containers

## AWS Container Services

- Amazon ECS: Designed to be able to integrate with other AWS services.
- Amazon EKS Elastic Container Services for Kubernetes. Easy to use Kubernetes on AWS Cloud
- Amazon ECR: Fully managed Docker Container Registry to store, manage and deploy Docker container images (just like Docker Hub). Integrated with ECS and EKS.

## ECR Create a registry

Login

```Shell
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin image
```

Create a repository

```Shell
aws ecr create-repository \
    --repository-name name \
    --image-scanning-configuration scanOnPush=true \
    --region us-east-1
```

Push. First create a tag with the repository URI locally.

```Shell
docker tag name image-name repositoryURI
docker push aws_account_id.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest
```

## Delete an image

```Shell
aws ecr batch-delete-image \
    --repository-name image-name
    --image-ids imageTag=tagName
```
