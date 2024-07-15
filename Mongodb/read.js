const { MongoClient } = require('mongodb');

async function main() {
    const uri = "mongodb://naim:AbcPassword123@localhost:27017";
    const client = new MongoClient(uri);

    try {
        await client.connect(); // Connect to the MongoDB cluster

        // Find the listing named "Beach house" in 'myDatabase'
        await findOneListingByName(client, "house 4");

        // Find listings with at least 4 bathrooms in 'myDatabase'
        await findListingsWithMinimumBathrooms(client, {
            minimumNumberOfBathrooms: 4,
            maximumNumberOfResults: 5
        });

    } finally {
        await client.close(); // Close the connection to the MongoDB cluster
    }
}

main().catch(console.error);

async function findOneListingByName(client, nameOfListing) {
    const result = await client.db("myDatabase").collection("listingsAndReviews").findOne({ name: nameOfListing });
    if (result) {
        console.log(`Found a listing in the collection with the name '${nameOfListing}':`);
        console.log(result);
    } else {
        console.log(`No listings found with the name '${nameOfListing}'`);
    }
}

async function findListingsWithMinimumBathrooms(client, {
    minimumNumberOfBathrooms = 0,
    maximumNumberOfResults = Number.MAX_SAFE_INTEGER
} = {}) {
    const cursor = client.db("myDatabase").collection("listingsAndReviews")
        .find({
            bathrooms: { $gte: minimumNumberOfBathrooms }
        })
        .sort({ last_review: -1 })
        .limit(maximumNumberOfResults);

    const results = await cursor.toArray();

    if (results.length > 0) {
        console.log(`Found listing(s) with at least ${minimumNumberOfBathrooms} bathrooms:`);
        results.forEach((result, i) => {
            const date = new Date(result.last_review).toDateString();
            console.log();
            console.log(`${i + 1}. name: ${result.name}`);
            console.log(` _id: ${result._id}`);
            console.log(` bathrooms: ${result.bathrooms}`);
            console.log(` most recent review date: ${date}`);
        });
    } else {
        console.log(`No listings found with at least ${minimumNumberOfBathrooms} bathrooms`);
    }
}
