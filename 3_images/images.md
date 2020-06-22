# Create own image

## Create a Docker File

You have to write down instructions to init the application.
The general configuration is:

1. OS
2. Update apt repo
3. Install dependencies using apt
4. Install Python dependencies using `pip`
5. Copy source code to /opt folder

A docker file is writed INSTRUCTION-ARGUMENT. Every docker image must be based on another image (OS).

All docker files must start with FROM instruction.

When docker builds images, it uses a Layered Architecture, each line builds a layer.
