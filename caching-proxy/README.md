# Caching Proxy

A caching server built with Go. This tool forwards requests to an origin server, caches responses, and improves performance on repeated requests.

---

## 📁 Folder Structure

```
caching-proxy/
├── proxy.go              # Main server implementation
├── go.mod                # Go module file
└── README.md             # Documentation and instructions
```

---

## ⚙️ Features

* Efficient response caching (using LRU cache)
* Fast performance using Go's concurrency
* Easy to extend for more advanced caching and request handling

---

## 🚀 Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/petrusjohannesmaas/caching-proxy.git
cd caching-proxy
```

### 2. Install Dependencies

Use the Go package manager to install the required external package:

```sh
go get github.com/hashicorp/golang-lru
```

### 3. Build the Project

```sh
go build -o caching-proxy proxy.go
```

### 4. Run the Proxy Server

```sh
./caching-proxy --port 3000 --origin http://dummyjson.com
```

### 5. Test the Proxy

Send a request to:

```
http://localhost:3000/products
```

You should receive the response from the origin and subsequent requests will hit the cache.

---

## 🧹 Clearing the Cache

To clear the cache manually, use:

```sh
./caching-proxy --clear-cache
```

> *(Make sure the CLI is updated to support this flag.)*

---

## 📦 Recommended Libraries

Consider these packages to enhance or optimize your proxy:

| Package                                                 | Description                                   |
| ------------------------------------------------------- | --------------------------------------------- |
| [`fasthttp`](https://github.com/valyala/fasthttp)       | High-performance HTTP server/client           |
| [`golang-lru`](https://github.com/hashicorp/golang-lru) | Simple and efficient LRU cache implementation |
| [`fiber`](https://github.com/gofiber/fiber)             | Express.js-style web framework for Go         |

---

## 🛠️ Future Enhancements

* Add TTL-based cache expiration
* Improve logging & error handling
* Support more HTTP methods (e.g., POST, PUT)
* Persist cache to disk between restarts
* Secure endpoint for manual cache invalidation

---
