#!/usr/bin/env node

const WebSocket = require("ws");

const args = process.argv.slice(2);
const command = args[0];
const port = 8080;

if (command !== "start") {
    console.error("Usage: broadcast-server start");
    process.exit(1);
}

const wss = new WebSocket.Server({ port });
console.log(`Broadcast server running at ws://localhost:${port}`);
wss.on("connection", (ws) => {
    console.log("Client connected.");

    ws.on("message", (message) => {
        try {
            console.log(`Broadcasting: ${message}`);
            wss.clients.forEach((client) => {
                if (client.readyState === WebSocket.OPEN) {
                    client.send(message.toString());
                }
            });
        } catch (err) {
            console.error("Error broadcasting message:", err);
        }
    });

    ws.on("error", (err) => {
        console.error("Client error:", err);
    });

    ws.on("close", () => console.log("Client disconnected."));
});

wss.on("error", (err) => {
    console.error("Server error:", err);
});

process.on("SIGINT", () => {
    console.log("\nGracefully shutting down server...");
    wss.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
            client.close(1001, "Server shutting down"); // 1001 = going away
        }
    });
    wss.close(() => {
        console.log("WebSocket server closed.");
        process.exit(0);
    });
});