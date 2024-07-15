const { MongoClient } = require('mongodb');

const dbUri = "mongodb://naim:AbcPassword123@localhost:27017";
const dbName = 'employees'; 

// Function to add a new employee
async function addEmployee(employeeData) {
    const client = new MongoClient(dbUri);
    try {
        await client.connect();
        const db = client.db(dbName);
        const employees = db.collection('employees');
        const result = await employees.insertOne(employeeData);
        console.log(`New employee added with the following id: ${result.insertedId}`);
    } catch (err) {
        console.error("Failed to add employee:", err.message);
    } finally {
        await client.close();
    }
}

// Function to retrieve all orders for a specific customer
async function getCustomerOrders(customerId) {
    const client = new MongoClient(dbUri);
    try {
        await client.connect();
        const db = client.db(dbName);
        const orders = db.collection('orders');
        const results = await orders.find({ customerId }).toArray();
        console.log(`Orders for customer ${customerId}:`, results);
        return results;
    } catch (err) {
        console.error("Failed to retrieve orders:", err.message);
    } finally {
        await client.close();
    }
}

// Function to update a product's quantity
async function updateProductQuantity(productId, newQuantity) {
    const client = new MongoClient(dbUri);
    try {
        await client.connect();
        const db = client.db(dbName);
        const products = db.collection('products');
        const result = await products.updateOne({ _id: productId }, { $set: { quantity: newQuantity } });
        console.log(`Product ${productId} updated with new quantity: ${newQuantity}`);
    } catch (err) {
        console.error("Failed to update product quantity:", err.message);
    } finally {
        await client.close();
    }
}

// Function to delete a user's account
async function deleteUserAccount(userId) {
    const client = new MongoClient(dbUri);
    try {
        await client.connect();
        const db = client.db(dbName);
        const users = db.collection('users');
        const result = await users.deleteOne({ _id: userId });
        if (result.deletedCount === 1) {
            console.log(`User account ${userId} successfully deleted.`);
        } else {
            console.log(`User account ${userId} not found.`);
        }
    } catch (err) {
        console.error("Failed to delete user account:", err.message);
    } finally {
        await client.close();
    }
}

module.exports = {
    addEmployee,
    getCustomerOrders,
    updateProductQuantity,
    deleteUserAccount
};
