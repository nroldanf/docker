# Docker basic commands

## **docker run**

Start a container from an image. It will run an instance of the image if already exists on the host, if not, it will download the image first.

The container will run and exit inmediatly. This is because docker containers are meant not to host an OS, but to run specific tasks or processes, so, once task is completed, containers exit.

To give a container a name, use `docker run --name container_name image_name`

To run a specific version use a tag `docker run container:tag`, _latest, for example.

Every container has a root command (displayed on COMMAND column). When this task is finished, the container will end.

**Containers only live as long as the processes live**

## **docker run -it**

Runs a container on interactive mode. The container does not stop inmediatly.

## **docker run --rm**

When exited the container, removed from system.

## **docker run --entrypoint**

Specifies entrypoint of the container.

## **docker run -p**

Maps a container port to a local port. Use a local_port:container_port syntax.

## **docker run -v**

Maps a directory of the container to a local directory. In other words, mount a external volume to a folder inside docker container. Useful to persist data on external volume. Use a local_directory:container_directory syntax.

## **docker run -d**

Runs a container on detached mode, runs in the background and you will be reprompted inmediatly.

## **docker run -e**

Sets enviroment variables within the container.

## **docker run --link**

Stablish connection between docker containers. DEPRECATED, use docker-compose networks instead.

## **docker attach**

Change to attach mode a container.

## **docker ps**

Shows all running containers and basic info about them (e.g. name of image, id, status, etc).

## **docker ps -a**

List all containers (running or not).

## **docker ps -aq**

List all containers IDS (useful for removing all and not one by one).

## **docker stop**

Stops a running container through SIGTERM. It's necesary to pass the docker container name or id.

## **docker rm**

Remove a docker container permanently from host. Can remove multiple containers specifying the names on sequence. Just few characters of CONTAINER_ID are necessary.

## **docker rm -f**

Remove docker containers even if these are running.

## **docker images/ docker image ls**

List available images and sizes.

## **docker rmi**

Remove docker image from host system. Same funcionality for removing multiple images as with rm command with containers.

**IMPORTANT:** Before remove any image, ensure if any dependent containers are running/or not first (use docker ps -a). You must stop and delete all dependant containers.

## **docker pull**

Download a docker image.

## **docker run image_name command**

You can append a command to run once container start.

## **docker exec**

Execute a command on a running container.

## **docker rename**

Rename an existing container.

## **docker logs**

Shows container's output even if is Exited (has been stopped). stdout.

## **docker kill**

Stop a running container through SIGKILL.

## **docker system prune**

Remove all dangling images, stopped containers, networks not used by at least one container and dangling build cache.

## **docker system df**

Shows total space used by docker resources (images, containers, volumes, build cache)

