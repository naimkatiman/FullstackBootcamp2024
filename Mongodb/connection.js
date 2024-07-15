const { MongoClient } = require('mongodb');

async function main() {
    // Include username and password in the URI for authentication
    const uri = "mongodb://naim:AbcPassword123@localhost:27017";

    const client = new MongoClient(uri);

    try {
        await client.connect(); // Connect to the database using authentication

        // Your DB operations here

    } catch (e) {
        console.error(e);
    } finally {
        await client.close(); // Close connection
    }
}

main().catch(console.error);
