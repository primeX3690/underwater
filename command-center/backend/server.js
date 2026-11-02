// command-center/backend/server.js
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const server = http.createServer(app);
const io = new Server(server, {
    cors: {
        origin: "*",
        methods: ["GET", "POST"]
    }
});

// सिमुलेटेड नेवल डेटाबेस / स्टेट
let activeNodes = 1000;
let networkMeshStatus = "HEALTHY_100_PERCENT";

io.on('connection', (socket) => {
    console.log(`[Command Center] Naval Officer connected: ${socket.id}`);

    // हर 3 सेकंड में नेवी वॉर रूम को लाइव टेलीमेट्री भेजना
    const telemetryInterval = setInterval(() => {
        const liveThreat = Math.random() < 0.15; // 15% चांस है कि कोई थ्रेट सिम्युलेट हो
        
        const telemetryPacket = {
            timestamp: new Date().toISOString(),
            activeNodes: activeNodes,
            meshStatus: networkMeshStatus,
            threatDetected: liveThreat,
            targetDetails: liveThreat ? {
                nodeId: Math.floor(Math.random() * 900) + 100,
                latitude: 8.5379 + (Math.random() * 0.1),
                longitude: 76.9313 + (Math.random() * 0.1),
                confidence: "98.4%",
                classification: "HOSTILE_DIESEL_SUBMARINE_PROPELLER"
            } : null
        };

        socket.emit('naval_telemetry_feed', telemetryPacket);
    }, 3000);

    socket.on('disconnect', () => {
        console.log(`[Command Centerdisconnected]: ${socket.id}`);
        clearInterval(telemetryInterval);
    });
});

const PORT = 5000;
server.listen(PORT, () => {
    console.log(`[War Room Server] Command Center Backend running on port ${PORT}`);
});