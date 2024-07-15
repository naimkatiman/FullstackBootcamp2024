const { MongoClient } = require('mongodb');

const dbUri = "mongodb://naim:AbcPassword123@localhost:27017";
const dbName = 'employees';

async function testConnection() {
    const client = new MongoClient(dbUri, { useNewUrlParser: true, useUnifiedTopology: true });
    try {
        await client.connect();
        console.log("Connected successfully to server");

        const db = client.db(dbName);
        const collection = db.collection('testCollection');

        const insertResult = await collection.insertOne({ testField: "testValue" });
        console.log("Insert result:", insertResult.insertedId);

        const databasesList = await client.db().admin().listDatabases();
        console.log("Databases:", databasesList.databases);
    } catch (err) {
        console.error("An error occurred:", err);
    } finally {
        await client.close();
    }
}

testConnection();
