# Create own image

An image is a template for containers.

A custom image is created when there is no image that satisfies your requirements. An image is created FROM other.

## Create a DockerFile

A DockerFile is the receipt for Docker images. You have to write down instructions to init the application. These instructions are wrote in a Dockerfile.
The general configuration (layered architecture) is:

1. OS
2. Install OS dependencies.
3. Create a Working directory.
4. Copy data into the image.
5. Create an entrypoint.

A docker file is writed INSTRUCTION-ARGUMENT. Every docker image must be based on another image (OS) o other image base on a OS.

All docker files must start with FROM instruction.

When docker builds images, it uses a Layered Architecture, each line builds a layer.

ENTRYPOINT is a command that will be run when a container based on that image runs.

## Layered Architecture

An image is build with layers, a base layer and layers that append to it. When an image is pulled, layers are download in parallel. Each Layer is INMUTABLE, each layer is difference with the layer before it (somewhat like git commits).

Docker reuse layers if there are images with different layers. Basically, the images are the same.

Layered architecture allows to restart the build since a checkpoint if failed or if you want to add additional steps. It will re-use layers from cache.

## Tools for exploring layes

- [Dive](<https://github.com/wagoodman/dive>)

## Tags

Images have different versions specified with a semicolon image:tag.

## **docker build**

Builds the image from a Dockerfile. It takes the path (e.g. ".", which is the pointer of the current folder) as parameter, build context send to Docker daemon.

## **docker build -f**

Specifies a docker file other than the default "Dockerfile".

## **docker commit**

It can be useful to commit new changes and configurations into a new image.

## **docker login**

Login with Docker ID to push and pull images from Docker Hub. First, is mandatory to create an account on DockerHub.

## **docker push**

Makes available on a public Docker Hub registry. It is necessary an organization to push image to DockerHub. By default, Docker points to docker.io/library/, where all official images are hosted.

Only the layers that do not exist on Docker Hub are pushed!!! :D

## **docker tag**

Creates a tag that points to the same layer of the image. This is made in order to, for example, push the image to our repository.

## **docker history**

Allows to see every layer in a docker image.

## **docker history --no-trunc**

Shows a verbose output of the each layer.
