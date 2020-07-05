FROM ubuntu:latest
LABEL author="Nicolás"
# Install Python and pip
RUN apt-get update -y && \
    apt-get install -y python-pip python3.6
# Make an /app directory for application
WORKDIR /app
# Copy all in the context into /app directory on container
COPY . /app
# Install Python dependencies
RUN pip --no-cache-dir install -r requirements.txt
# Launch python3 interpreter
ENTRYPOINT [ "python" ]
# Run this command as default when runs a container
CMD ["app.py"]