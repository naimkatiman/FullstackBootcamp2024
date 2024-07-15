const express = require('express');
const app = express();
const port = 3000;
const itemsRouter = require('./routes/items');

app.use('/items', itemsRouter);

app.listen(3000, () => console.log('Server running on http://localhost:3000'))

app.use(express.json());

let items = [];

// Get all items
app.get('/items', (req, res) => {
  res.json(items);
});

// Create a new item
app.post('/items', (req, res) => {
  const item = { id: items.length + 1, ...req.body };
  items.push(item);
  res.status(201).send(item);
});

// Get a single item by ID
app.get('/items/:id', (req, res) => {
  const item = items.find(i => i.id === parseInt(req.params.id));
  if (!item) return res.status(404).send('Item not found');
  res.send(item);
});

// Update an item by ID
app.put('/items/:id', (req, res) => {
  const item = items.find(i => i.id === parseInt(req.params.id));
  if (!item) return res.status(404).send('Item not found');

  item.name = req.body.name;
  res.send(item);
});

// Delete an item by ID
app.delete('/items/:id', (req, res) => {
  const index = items.findIndex(i => i.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).send('Item not found');

  items.splice(index, 1);
  res.status(204).send();
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
