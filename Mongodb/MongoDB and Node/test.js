const { addEmployee, getCustomerOrders, updateProductQuantity, deleteUserAccount } = require('./employees');

async function runDatabaseOperations() {
    try {
        const employeeData = {
            name: "John Doe",
            role: "Software Engineer",
            department: "Development"
        };

        await addEmployee(employeeData);
        console.log("Employee added successfully.");

        const customerId = "customer123";  // Ensure this ID exists in your database for testing
        const orders = await getCustomerOrders(customerId);
        console.log("Retrieved orders for customer:", orders);

        const productId = "product456";  // Ensure this ID exists in your database for testing
        const newQuantity = 50;
        await updateProductQuantity(productId, newQuantity);
        console.log("Product quantity updated successfully.");

        const userId = "user789";  // Ensure this ID exists in your database for testing
        await deleteUserAccount(userId);
        console.log("User account deleted successfully.");
    } catch (err) {
        console.error("An error occurred:", err);
    }
}

runDatabaseOperations();
