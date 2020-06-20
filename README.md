# docker

## Docker Setup and Installation

First you have to verify the requirements for your OS.
Docker is only available for Windows PRO, Mac and various linux distributions (Ubuntu, Fedora, etc).

```shell
cat /etc/*release*
```

### 1. Download docker from repository

Update package index

`sudo apt-get update`

Install packages to allow `apt` to use a repo over HTTPS

```shell
sudo apt-get install\
    apt-transport-https\
    curl\
    software-properties-common
```

Add Docker's official GPG key (for identity validation of repo)

```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

For x86_64/amd64 processor architecture

```shell
sudo add-apt-repository \
   \"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   (lsb_release -cs) \
   stable\"
```

Reference: [Docker Installation Ubuntu](<https://docs.docker.com/engine/installubuntu/>)

### 2. Install Docker CE

Install Latest version of Docker CE. Once finished, Docker will be working as a Daemon.

```shell
sudo apt-get update
sudo apt-get install docker-ce
```

Verify the version

```shell
sudo docker --version
```

Give permission to non-super user to use docker. This is a good practice, so we don't have to use sudo every time.

```shell
sudo usermod -aG docker nicolas
exit
```

## Docker Setup and Installation with convenience script

You also can use the **convenience script** to install docker. First line download the shell script and second execute it.

```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

Run a simple container to ensure is working as expected. Go to [Docker Hub](<https://hub.docker.com/>) to find a docker Image. A good one is [docker/whalesay](<https://hub.docker.com/r/docker/whalesay>)

```shell
docker run docker/whalesay cowsay hola mundo
```

If docker does not find image locally, it will download it.
