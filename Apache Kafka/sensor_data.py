from confluent_kafka import Producer
import json
import time
import random

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result. Triggered by poll() or flush(). """
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Create a Producer instance
conf = {'bootstrap.servers': "localhost:9092"}
producer = Producer(conf)

# Function to generate random sensor data
def generate_sensor_data():
    return {
        'sensor_id': random.randint(1, 100),
        'timestamp': int(time.time()),
        'temperature': round(random.uniform(20.0, 30.0), 2),
        'humidity': round(random.uniform(30.0, 70.0), 2)
    }

# Produce data to Kafka topic
for _ in range(10):
    sensor_data = generate_sensor_data()
    producer.produce('sensor_data', key=str(sensor_data['sensor_id']), value=json.dumps(sensor_data), callback=delivery_report)
    producer.poll(1)
    time.sleep(1)

# Wait for any outstanding messages to be delivered and delivery report callbacks to be triggered
producer.flush()
