// Import MongoDB client
const { MongoClient } = require('mongodb');

// MongoDB connection URI and database name
const uri = "mongodb://localhost:27017"; // Replace with your actual MongoDB URI
const dbName = 'mydb'; // Replace with your database name

// Create a new MongoClient
const client = new MongoClient(uri);

async function main() {
    try {
        // Connect to the MongoDB server
        await client.connect();
        console.log("Successfully connected to Database");

        // Get the database and collection
        const database = client.db(dbName);
        const collection = database.collection('newcol');

        // Insert documents
        const insertResult1 = await collection.insertOne({
            name: "Miao",
            species: "cat"
        });
        const insertResult2 = await collection.insertOne({
            name: "Joaquin",
            species: "Human"
        });

        // Find documents
        const findResult = await collection.find({name: "Miao"}).toArray();
        console.log('Found documents:', findResult);

        // Update a document
        const updateResult = await collection.findOneAndUpdate(
            { name: "Miao" }, 
            { $set: { name: "Mittens" } },
            { returnOriginal: false }
        );
        console.log('Updated Document:', updateResult.value);
    } finally {
        // Close the connection
        await client.close();
    }
}

// Run the main function and catch any errors
main().catch(console.error);
