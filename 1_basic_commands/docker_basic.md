# Docker basic commands

## **docker run**

Start a container from an image. It will run an instance of the image if already exists on the host, if not, it will download the image first.

The container will run and exit inmediatly. This is because docker containers are meant not to host an OS, but to run specific tasks or processes, so, once task is completed, containers exit.

**Containers only live as long as the processes live**

## **docker run -it**

Runs a container on interactive mode. The container does not stop inmediatly.

## **docker run -d**

Runs a container on detached mode, runs in the background and you will be reprompted inmediatly.

## **docker attach**

Change to attach mode a container.

## **docker ps**

Shows all running containers and basic info about them (e.g. name of image, id, status, etc).

## **docker ps -a**

Shows all containers (running or not).

## **docker stop**

Stops a container. It's necesary to pass the docker container name or id.

## **docker rm**

Remove a docker container permanently from host. Can remove multiple containers specifying the names on sequence. Just few characters of CONTAINER_ID are necessary.

## **docker images**

List available images and sizes.

## **docker rmi**

Remove docker image from host system.

**IMPORTANT:** Before remove any image, ensure if any dependent containers are running first. You must stop and delete all dependant containers.

## **docker pull**

Download a docker image.

## **docker run image_name command**

You can append a command to run once container start.

## **docker exec**

Execute a command on a running container.
