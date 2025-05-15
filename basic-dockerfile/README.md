# Basic Dockerfile Project

This project contains a simple Dockerfile that, when built and run, outputs “Hello, Captain!” with the active user and the date to the console.

### Getting Started
These instructions will guide you through building and running the Docker image.

**Prerequisites**
Ensure you have Docker installed on your machine. You can download and install Docker from here.

### Instructions

Clone the repository (if applicable):

```sh
git clone https://github.com/TalalNuman/hello-docker.git
cd hello-docker
```

### Build the Docker image:

Run the following command to build the Docker image using the Dockerfile in the root directory:

```sh
docker build -t hello-captain .
Run the Docker container:
```

After building the image, you can run and delete the container using:

```sh
docker run --rm hello-captain
```
