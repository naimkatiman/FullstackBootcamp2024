const express = require('express');
const bcrypt = require('bcrypt');
const app = express();
const port = 3000;
app.use(express.json());

let users = [];

// Register a new user
app.post('/register', async (req, res) => {
  const { username, password } = req.body;

  // Check if username already exists
  if (users.find(user => user.username === username)) {
    return res.status(400).json({ message: 'Username already exists' });
  }

  // Hash the password
  const hashedPassword = await bcrypt.hash(password, 10);

  // Save the user
  users.push({ username, password: hashedPassword });
  res.status(201).json({ message: 'User registered successfully' });
});

// Log in
app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  // Find the user by username
  const user = users.find(user => user.username == username);
  if (!user) {
    return res.status(401).json({ message: 'Invalid username or password' });
  }

  // Check the password
  const validPassword = await bcrypt.compare(password, user.password);
  if (!validPassword) {
    return res.status(401).json({ message: 'Invalid username or password' });
  }

  res.status(200).json({ message: 'Logged in successfully' });
});

// Log out
app.delete('/logout', (req, res) => {
  // Log out logic here
  res.status(200).json({ message: 'Logged out successfully' });
});

app.listen(3000, () => {
    console.log(`Server running at http://localhost:${port}`);
});