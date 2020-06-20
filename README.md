# docker

Docker snippets

## 1. Docker configuration on Ubuntu-Linux (using repository)

Update package index

`sudo apt-get update`

Install packages to allow `apt` to use a repo over HTTPS

```shell
sudo apt-get install\
    apt-transport-https\
    curl\
    software-properties-common
```

Add Docker's official GPG key

```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

