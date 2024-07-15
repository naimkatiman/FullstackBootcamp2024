const express = require('express');
const app = express();
const PORT = 3001;

app.use(express.json());

// POST route for login
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    if (username === "ja" && password === "password123") {
        res.status(200).send({ message: "Login successful!" });
    } else {
        res.status(401).send({ message: "Invalid credentials" });
    }
});

// GET and POST routes for products
app.get('/products', (req, res) => {
    res.send({ products: ["rendang", "ketupat", "lemang"] });
});

app.post('/products', (req, res) => {
    const { product } = req.body;
    if (product) {
        res.status(201).send({ message: `Product ${product} added successfully!` });
    } else {
        res.status(400).send({ message: "No product provided" });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
