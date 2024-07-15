from confluent_kafka import Consumer, KafkaException, KafkaError
import json

# Create a Consumer instance
conf = {
    'bootstrap.servers': "localhost:9092",
    'group.id': "sensor_data_group",
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(conf)

# Subscribe to the topic
consumer.subscribe(['sensor_data'])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print(f"{msg.topic()} [{msg.partition()}] reached end at offset {msg.offset()}")
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            # Proper message
            sensor_data = json.loads(msg.value().decode('utf-8'))
            print(f"Received message: {sensor_data}")

except KeyboardInterrupt:
    pass
finally:
    # Close down consumer to commit final offsets.
    consumer.close()
