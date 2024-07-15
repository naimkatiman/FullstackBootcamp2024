const express = require('express');
const app = express();
const PORT = 3000;


app.use(express.json());

let movies = [];
let directors = [];
let actors = [];

// Movies routes
app.post('/movies', (req, res) => {
    movies.push(req.body);  
    res.status(201).send('Movie added.');
});

app.get('/movies', (req, res) => {
    res.status(200).json(movies.map((movie, index) => ({ id: index, ...movie })));
});

app.get('/movies/:id', (req, res) => {
    const index = parseInt(req.params.id);
    if (index >= 0 && index < movies.length) {
        const movie = { id: index, ...movies[index] };
        res.status(200).json(movie);
    } else {
        res.status(404).send('Movie not found.');
    }
});

app.put('/movies/:id', (req, res) => {
    const index = parseInt(req.params.id);
    if (index >= 0 && index < movies.length) {
        movies[index] = req.body; 
        res.status(200).send('Movie updated.');
    } else {
        res.status(404).send('Movie not found.');
    }
});

app.delete('/movies/:id', (req, res) => {
    const index = parseInt(req.params.id);
    if (index >= 0 && index < movies.length) {
        movies.splice(index, 1); 
        res.status(200).send('Movie deleted.');
    } else {
        res.status(404).send('Movie not found.');
    }
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
