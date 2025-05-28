#!/usr/bin/env node

const WebSocket = require("ws");
const readline = require("readline");

const args = process.argv.slice(2);
const command = args[0];
const serverUrl = "ws://server:8080";

if (command !== "connect") {
    console.error("Usage: broadcast-server connect");
    process.exit(1);
}

const ws = new WebSocket(serverUrl);

ws.on("open", () => {
    console.log(`Connected to ${serverUrl}`);

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    let nickname = process.env.NICKNAME || "anonymous";

    // Prompt for nickname
    rl.question("Enter your nickname: ", (name) => {
        if (name.trim()) nickname = name.trim();

        rl.setPrompt(`${nickname}> `);
        rl.prompt();

        // Read input line by line
        rl.on("line", (msg) => {
            try {
                const formattedMsg = `${nickname}: ${msg}`;
                ws.send(formattedMsg);
            } catch (err) {
                console.error("Failed to send message:", err);
            }
            rl.prompt();
        });
    });
});


ws.on("error", (err) => {
    console.error("Connection error:", err);
});


ws.on("message", (data) => console.log(`Received: ${data}`));
ws.on("close", () => {
    console.log("Disconnected.");
    process.exit(0);
});