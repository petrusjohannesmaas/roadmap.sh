# Basic Dockerfile Project

This project contains a simple Dockerfile that, when built and run, outputs “Hello, Captain!” with the active user and the date to the console.

**Prerequisites:**
Ensure you have Docker installed on your machine. You can download and install Docker from [here](https://docs.docker.com/get-started/get-docker/):

### Instructions

Clone my `roadmap.sh` repository (if applicable):

```sh
git clone https://github.com/petrusjohannesmaas/roadmap.sh.git
cd basic-dockerfile
```

### Build the Docker image:

Run the following command to build the Docker image using the Dockerfile in the root directory:

```sh
docker build -t hello-captain .
```

After building the image, you can run (and delete) the container using:
```sh
docker run --rm hello-captain
```
