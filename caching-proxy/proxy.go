go
package main

import (
	"flag"
	"fmt"
	"io"
	"net/http"
	"github.com/hashicorp/golang-lru"
)

var (
	port   int
	origin string
	cache  *lru.Cache
)

func fetchAndCache(w http.ResponseWriter, req *http.Request) {
	url := origin + req.URL.Path

	resp, err := http.Get(url)
	if err != nil {
		http.Error(w, "Error fetching data", http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()

	data, err := io.ReadAll(resp.Body)
	if err != nil {
		http.Error(w, "Error reading response", http.StatusInternalServerError)
		return
	}

	cache.Add(req.URL.Path, data) // LRU caching

	w.Header().Set("X-Cache", "MISS")
	w.Write(data)
}

func handler(w http.ResponseWriter, req *http.Request) {
	if data, ok := cache.Get(req.URL.Path); ok {
		// Serve cached response
		w.Header().Set("X-Cache", "HIT")
		w.Write(data.([]byte))
	} else {
		// Fetch and cache response
		fetchAndCache(w, req)
	}
}

func main() {
	flag.IntVar(&port, "port", 3000, "Port for proxy server")
	flag.StringVar(&origin, "origin", "", "Origin server URL")
	flag.Parse()

	if origin == "" {
		fmt.Println("Usage: caching-proxy --port <number> --origin <url>")
		return
	}

	var err error
	cache, err = lru.New(100) // Limit cache size to 100 entries
	if err != nil {
		fmt.Println("Error initializing cache:", err)
		return
	}

	http.HandleFunc("/", handler)
	fmt.Printf("Caching proxy server running on port %d, forwarding to %s\n", port, origin)
	http.ListenAndServe(fmt.Sprintf(":%d", port), nil)
}