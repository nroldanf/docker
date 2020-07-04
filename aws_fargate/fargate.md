# Fargate in action

## With ECS

- __Task Definition:__ Define application containers: image, CPU and Memory
- __Task Running:__ Running instantiation of a task definition.
- __Cluster:__ Infrastructure isolation boundary.
- Service

## Task Definition

- Inmutable document.
- Identified by family: version.
- Contains a list up to 10 container definitions.
- All containers are collocated on the same host.

Each container definition has:

- Name
- Image URL (Amazon ECR or Public Images)

### 1. Compute Resources

Task level Resources:

- Total CPU across all containers.
- Memory in MB
- 1 vCPU = 1024 cpu-units

Container Level Resources

- Defines sharing of task resources among containers.

Around 50 different combinations of resources (Important for pricing)

### 2. Networking

### 3. Storage

Amazon EBS backed ephemeral storage provided in the form of:

The topmost layer of a docker image is a writable layer to capture file changes made bu the running container.

- Writable Layer Storage (on top): 10 GB storage available per task.
- Volume Storage: 4GB volume space per task. Writes visible across containers.

When a task stop, data is deleted after task stops.

If need persitance, push data into S3 or Dynamo.

### 4. IAM Permissions

Who can lauch tasks in my cluster.

__Application permissions:__ Allows application containersto access AWS Resources securely.

Housekeeping Permission:

- __Execution Role__: For ECR image pull and pushing cloudwatch logs (awslogs driver)

- __ECS Service Linked Role__: ENI management, and ELB target registration. Automatically create by AWS.

### 5. Monitoring

awslogs.
