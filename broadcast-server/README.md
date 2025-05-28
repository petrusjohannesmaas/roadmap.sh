# 📡 WebSocket Broadcast App with Docker (Node.js + ws)

This guide walks you through:

* Building a WebSocket broadcast server
* Connecting CLI clients
* Containerizing both server and client with **Docker**
* Running everything using **Docker Compose**

---

## ✅ Prerequisites

* Docker
* Docker Compose

---

## 📁 Project Structure

```
broadcast-app/
│
├── server/
│   ├── server.js
│   ├── package.json
│   ├── Dockerfile
│
├── client/
│   ├── client.js
│   ├── package.json
│   ├── Dockerfile
│
└── docker-compose.yml
```

---

## 🐳 Dockerfiles (same as before)

No changes needed to the Dockerfiles — Docker and Podman both support them.

---

## 🔧 Docker Compose File

**`docker-compose.yml`**

```yaml
version: "3"
services:
  server:
    build: ./server
    ports:
      - "8080:8080"

  client:
    build: ./client
    depends_on:
      - server
    stdin_open: true
    tty: true
```

---

## 🚀 Step-by-Step Commands

### Build and Start Services

```sh
docker-compose up --build -d
```

### Run Clients Interactively

```sh
docker-compose run client
```

Run this command multiple times in different terminals to simulate multiple clients.

---

## 🛑 Shut Down and Clean Up

```sh
docker-compose down
```

Optional:

```sh
docker image prune -a
```

---

### Future Enhancements:

* Convert to TypeScript
* gRPC instead of WebSockets
* Encryption
* Authentication

---