const express = require("express");
const app = express();
const morgan = require("morgan");
const bodyParser = require("body-parser");

const productRoutes = require("./api/routes/products")
const orderRoutes = require("./api/routes/orders")

app.use(morgan("dev")); 
app.use(bodyParser.urlencoded({ extended:false}));
app.use(bodyParser.json());

app.use("/products", productRoutes);
app.use("/orders", orderRoutes);

// Middleware to handle 404 errors 
app.use((req, res, next) => {
    const error = new Error("Not found");
    error.status = 404;
    next(error);
});

// Error handling middleware for 500 errors 
app.use((error, req, res, next) => {
    res.status(error.status || 500)
    req.json({
        error: {
            message: error.message
        }     
    });
});

module.exports = app;