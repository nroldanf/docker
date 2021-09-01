#!/bin/sh
# References: https://blog.mapbox.com/aws-lambda-python-magic-e0f6a407ffc6
echo "Python runtime: $1"
# Create the file system structure for installing packages
DIRECTORY="python/lib/python$1/site-packages/"
DOCKER_IMAGE="lambci/lambda:build-python$1"
# Make a directory where to save the packages
mkdir -p $DIRECTORY
# cd $DIRECTORY
# Pull docker image corresponding to the python runtime
echo "Pulling the image..."
docker pull $DOCKER_IMAGE
# Run pip install inside the docker container
echo "Installing python dependencies..."
docker run --rm -it -v $(pwd):/var/task $DOCKER_IMAGE pip install -r requirements.txt $2 -t $DIRECTORY
# Remove info directories
echo "Removing unnecessary files and directories..."
find $DIRECTORY -name "*-info" -type d -exec rm -rdf {} +
# Remove tests scripts directories
find $DIRECTORY -name "tests" -type d -exec rm -rdf {} +
# Remove packages that will be present in lambda environment (e.g. botocore and boto3)
rm -rdf $DIRECTORY/boto3/
rm -rdf $DIRECTORY/botocore/
echo "Compressing final package..."
# Compress with zip the resulting directory
zip -rq "package.zip" "python/"
# # Remove the directory
rm -rf "python/"
echo "DONE!!!"
