# Dockerfile instructions

## **FROM**

Specifies base image. If scratch is the value, the only thing available in the image is the linux kernel.

## **ENV**

Defines enviroment variables.

## **COPY**

Copies all files from a directory to a directory inside the docker container based on the image.

## **WORKDIR**

Changes the current directory to other (just like cd on linux).

## **RUN**

Runs commands on the terminal.

## **EXPOSE**

Exposes a port of the container.

## **ENTRYPOINT**

Defines base command to run to which entry command when container runs will be appended. When no command instruction is specified and a CMD instruction follows this one, CMD parameter will be appended by default.

## **CMD**

Defines default command that will run when the container runs. If a command is explicitly specified, is CMD command is overwrited.
