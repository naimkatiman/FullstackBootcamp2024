// listDatabases.js
const { MongoClient } = require('mongodb');

const url = 'mongodb://localhost:27017';

const client = new MongoClient(url, { useNewUrlParser: true, useUnifiedTopology: true });

async function listDatabases() {
    try {
        await client.connect();
        console.log("Connected successfully to server");
        const databasesList = await client.db().admin().listDatabases();

        console.log("Databases:");
        databasesList.databases.forEach(db => console.log(` - ${db.name}`));
    } catch (error) {
        console.error("Failed to retrieve database list:", error);
    } finally {
        await client.close();
    }
}

listDatabases();
