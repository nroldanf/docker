# Create own image

A custom image is created when there is no image that satisfies your requirements. An image is created FROM other.

## Create a Docker File

You have to write down instructions to init the application. These instructions are wrote in a Dockerfile.
The general configuration (layered architecture) is:

1. OS
2. Install OS dependencies.
3. Create a Working directory.
4. Copy data into the image.
5. Create an entrypoint.

A docker file is writed INSTRUCTION-ARGUMENT. Every docker image must be based on another image (OS) o other image base on a OS.

All docker files must start with FROM instruction.

When docker builds images, it uses a Layered Architecture, each line builds a layer.

## Layered Architecture

Layered architecture allows to restart the build since a checkpoint if failed or if you want to add additional steps. It will re-use layers from cache.

## **docker build**

Builds the image from a Dockerfile.

## **docker login**

Login with Docker ID to push and pull images from Docker Hub. First, is mandatory to create an account on DockerHub.

## **docker push**

Makes available on a public Docker Hub registry. It is necessary an organization to push image to DockerHub.
