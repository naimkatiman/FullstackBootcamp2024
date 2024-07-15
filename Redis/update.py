import redis

r = redis.Redis(host='localhost', port=6379)

def update_product_with_pipeline(product):
    product_id = product['id']
    increment_quantity = product['quantity']
    new_price = product['price']

    # Pipeline
    with r.pipeline() as pipe:
        pipe.hincrby(f"product:{product_id}", "quantity", increment_quantity)
        pipe.hset(f"product:{product_id}", "price", new_price)
        pipe.execute()

    
    updated_product = r.hgetall(f"product:{product_id}")

    updated_product = {key.decode(): value.decode() for key, value in updated_product.items()}
    print(f"Updated product details: {updated_product}")

# Sample product 
sample_product = {
    'id': '1234',
    'quantity': 10,
    'price': 199.99
}

update_product_with_pipeline(sample_product)
