const express = require('express');
const app = express();
const port = 3001;
const path = require ('path');

// Route for /hello
app.get('/hello', (req, res,) =>{
    res.json({message: 'Hello, welcome to your first API!'})
});

// Route for /about
app.get('/about', (req, res,) =>{
    res.json({message: 'This is a simple API made with the Express'})
});

//Route for /image
app.get('/image', (req, res) => {
const imagePath = path.join(__dirname, 'cat.png');
res.sendFile(imagePath);
});

// Route for /users
app.get('/users', (req, res) => {
    res.json([
        { id: 1, name: 'Minah' },
        { id: 2, name: 'Siti' },
        { id: 3, name: 'Joyah' },
        { id: 4, name: 'Ameng' },
        { id: 5, name: 'Ketupat' }
    ]);
});

// Route for /text
app.get('/text', (req, res) => {
    res.type('text/plain');
    res.send('Testing plain message 123');
});

// Route for /status
app.get('/status', (req, res) => {
    res.json({ status: 'Server is healthy', uptime: process.uptime() });
});

// Start the server
app.listen(port, () =>{
    console.log(`Server is running at http://localhost:${port}`);
});