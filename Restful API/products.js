const express = require('express');
const bcrypt = require('bcrypt');
const app = express();
const port = 3000;

app.use(express.json());

let users = [];
let products = [];

// Register a new user
app.post('/register', async (req, res) => {
  const { username, password } = req.body;
  if (users.find(user => user.username === username)) {
    return res.status(400).json({ message: 'Username already exists' });
  }
  const hashedPassword = await bcrypt.hash(password, 10);
  users.push({ username, password: hashedPassword });
  res.status(201).json({ message: 'User registered successfully' });
});

// Log in
app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const user = users.find(user => user.username == username);
  if (!user) {
    return res.status(401).json({ message: 'Invalid username or password' });
  }
  const validPassword = await bcrypt.compare(password, user.password);
  if (!validPassword) {
    return res.status(401).json({ message: 'Invalid username or password' });
  }
  res.status(200).json({ message: 'Logged in successfully' });
});

// Log out
app.delete('/logout', (req, res) => {
  res.status(200).json({ message: 'Logged out successfully' });
});

// Add a new product
app.post('/products', (req, res) => {
  const { name, price } = req.body;
  if (!name || !price) {
    return res.status(400).json({ message: 'Product name and price are required' });
  }
  products.push({ name, price });
  res.status(201).json({ message: 'Product added successfully' });
});

// Get products (with optional filtering by name)
app.get('/products', (req, res) => {
  const { name } = req.query;
  if (name) {
    const filteredProducts = products.filter(product => product.name.toLowerCase() === name.toLowerCase());
    if (filteredProducts.length) {
      res.status(200).json(filteredProducts);
    } else {
      res.status(404).json({ message: 'No products found with that name' });
    }
  } else {
    res.status(200).json(products);
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
