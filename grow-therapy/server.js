import http from 'http';

import router from "./router.js";

const hostname = '127.0.0.1';
const port = 3000;

// Listener (data unpacker)
function requestListener (req, res, callback) {
    res.setHeader('Content-Type', 'application/json');
    let body = '';
    req.on('data', chunk => {
        body += chunk.toString();
    });
    req.on('end', () => {
        callback(res, req, JSON.parse(body));
    });
}

// Server
const server = http.createServer((req, res) => {
    requestListener(req, res, router)
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
