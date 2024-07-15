const express = require('express');
const router = express.Router();

// GET route to fetch orders
router.get('/', (req, res, next) => {
    res.status(200).json({
        message: 'Handling GET requests to /orders'
    });
});

// POST route to create a new order
router.post('/', (req, res, next) => {
    const order = {
        productId: req.body.productId,
        quantity: req.body.quantity
    };
    res.status(201).json({
        message: 'Handling POST requests to /orders',
        createdOrder: order
    });
});

module.exports = router;
