const express = require('express');
const router = express.Router();

// GET route to fetch all products
router.get('/', (req, res, next) => {
    res.status(200).json({
        message: 'Handling GET requests to /products'
    });
});

// GET route with dynamic productId
router.get('/:productId', (req, res, next) => {
    const productId = req.params.productId;
    if (productId === 'special') {
        res.status(200).json({
            message: 'You are special!',
            productId: productId
        });
    } else {
        res.status(200).json({
            message: 'Handling GET requests for product',
            productId: productId
        });
    }
});

// POST route to add a new product
router.post('/', (req, res, next) => {
    const product = {
        name: req.body.name,
        price: req.body.price
    };
    res.status(201).json({
        message: 'Product created',
        createdProduct: product
    });
});

module.exports = router;
