# 📡 CLI WebSocket Chat App

A simple CLI-based WebSocket broadcast app built with Node.js. This tool lets you:

* Start a WebSocket server
* Connect multiple interactive clients via terminal
* Broadcast messages between connected clients in real-time
* Gracefully handle disconnections with `Ctrl+C`

**Prerequisites:** Make sure you have Node.js installed on your machine.

## ✅ Features

* Terminal-based real-time messaging
* Nickname support
* Broadcast to all connected clients
* Graceful shutdown (`Ctrl+C`)
* Clean architecture: server and client logic separated

## 🧠 How It Works


| Command                    | Description                      |
| -------------------------- | -------------------------------- |
| `broadcast-server start`   | Starts the WebSocket server      |
| `broadcast-server connect` | Connects a terminal-based client |

All clients connect to the server and send messages that are broadcast to all other connected clients.


## 📁 Project Structure

```
broadcast-app/
│
├── broadcast-server.js   # Main CLI entry point
├── server.js             # Server logic
├── client.js             # Client logic
├── package.json
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/petrusjohannesmaas/roadmap.sh/
cd broadcast-server
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Link the CLI Command

```bash
chmod +x broadcast-server.js
sudo npm link
```

This will let you run `broadcast-server` globally from anywhere.

## 📦 Usage

**Start the WebSocket Server:**

```bash
broadcast-server start
```

* Starts the server on `ws://localhost:8080`
* Logs client connections and broadcasts

**Connect Clients:**

Run these commands in separate terminals to simulate multiple clients.

```bash
broadcast-server connect
```

* Prompts for a nickname
* Lets you send messages interactively
* Messages are broadcast to all other connected clients


## 🔧 Future Customization Ideas

* Add command line options (`--port`, `--nickname`)
* Add secure WebSocket (`wss://`) support
* Add user authentication
* Add message history or logging
* Convert to TypeScript
* Migrate to Deno from Node
* gRPC or GraphQL API


## 🧪 Example Session

**Terminal A:**

```bash
broadcast-server start
# Output: Broadcast server running at ws://localhost:8080
```

**Terminal B:**

```bash
broadcast-server connect
Enter your nickname: Alice
Alice> Hello!
```

**Terminal C:**

```bash
broadcast-server connect
Enter your nickname: Bob
Bob> Hey Alice!
# Terminal B sees: Received: Bob: Hey Alice!
```

## 🛑 Graceful Shutdown

* Press `Ctrl+C` in any terminal to disconnect
* Server will notify all clients and close connections
