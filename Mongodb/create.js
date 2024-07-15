const {MongoClient} = require('mongodb');

async function main(){
    const uri = "mongodb://naim:AbcPassword123@localhost:27017";

    const client = new MongoClient(uri);

    try{
        // Connecting to db 
        await client.connect();
        
        await createListing (client,
            {
                name: "House 1",
                summary: "A nice hourse",
                bedrooms: 1,
                bathrooms: 1
            }
        );

        // insert 3 documents db.collection.insertMany([{}, {}, {}])
        await createMultipleListings(client, [
            {
                name: "House 2",
                summary: "A nice horse",
                bedrooms: 3,
                bathrooms: 2,
                beds: 5
            },
            {
                name: "House 3",
                summary: "Penthouse",
                bedrooms: 4,
                bathrooms: 4,
                beds: 8,
                last_review: new Date()
            },
            {
                name: "House 4",
                summary: "Beach house",
                bedrooms: 5,
                bathrooms: 4,
                beds: 2,
                location: "Bali",
                last_review: new Date()
            }
        ]);
    } finally{
        // Close connection
        await client.close();
    }
}

main().catch(console.error);

//Creating one listing (insertOne)
async function createListing(client, newListing){
    const result = await client.db("sample_airbnb").collection("listingsAndReviews").insertOne(newListing);
    console.log(`New listing created with the following ID: ${result.insertedId}`);
}

async function createMultipleListings(client, newListings){
    const result = await client.db("sample_airbnb").collection("listingsAndReviews").insertMany(newListings);
    console.log(`New listing(s) created with the following IDs: `);
    console.log(result.insertedIds);
}