import os
import time
import subprocess
import signal

def start_process(command):
    return subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def stop_process(process):
    process.send_signal(signal.SIGINT)
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()

# Define the Kafka home directory
KAFKA_HOME = os.path.expanduser("~/kafka_2.13-3.7.0")

# Start Zookeeper
zk_command = f"{KAFKA_HOME}/bin/zookeeper-server-start.sh {KAFKA_HOME}/config/zookeeper.properties"
zk_process = start_process(zk_command)
print("Zookeeper started")

# Wait a few seconds to ensure Zookeeper starts before Kafka
time.sleep(5)

# Start Kafka broker
kafka_command = f"{KAFKA_HOME}/bin/kafka-server-start.sh {KAFKA_HOME}/config/server.properties"
kafka_process = start_process(kafka_command)
print("Kafka broker started")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Terminating processes")
    stop_process(kafka_process)
    stop_process(zk_process)
    print("Processes terminated")
