import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

product = {
    'id': 'myProduct',
    'quantity': 100,
    'price': 10.99
}

# Function to set the initial product in Redis
def set_initial_product(redis_client, product):
    try:
        # Set initial product values
        redis_client.hset(product['id'], mapping={'quantity': product['quantity'], 'price': product['price']})
    except redis.RedisError as e:
        print(f"Error setting initial product {product['id']}: {e}")

# Function to update the product in Redis
def update_product(redis_client, product):
    try:
        # Use pipeline to execute multiple commands
        with redis_client.pipeline() as pipe:
            # Update product quantity
            pipe.hincrby(product['id'], 'quantity', 50)

            # Update product price
            pipe.hset(product['id'], 'price', 9.99)

            # Execute pipeline
            pipe.execute()

    except redis.RedisError as e:
        print(f"Error updating product {product['id']}: {e}")

# Set initial product in Redis
set_initial_product(r, product)

# Test update function
update_product(r, product)

# Verify updates
updated_quantity = r.hget(product['id'], 'quantity').decode('utf-8')
updated_price = r.hget(product['id'], 'price').decode('utf-8')

print(f"Updated quantity: {updated_quantity}")
print(f"Updated price: {updated_price}")

# Retrieve and print all fields and values of the product
product_details = r.hgetall(product['id'])
for key, value in product_details.items():
    print(f"{key.decode('utf-8')}: {value.decode('utf-8')}")
