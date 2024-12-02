import pytest
import paho.mqtt.client as mqtt
import time
import uuid  # To generate unique topic IDs
import warnings

# Broker and topic settings
BROKER = "test.mosquitto.org"
PORT = 1883
TIMEOUT = 20  # Timeout for connection
RETRIES = 5  # Number of retries before failure
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Generate a unique topic ID
unique_topic = f"test/topic/{uuid.uuid4()}"  # Generate a unique topic for each test
@pytest.fixture
def mqtt_client():
    # Create a new MQTT client instance
    client = mqtt.Client()

    # Add a custom flag to track connection status
    client.connected_flag = False

    # Define the on_connect callback to handle the connection result
    def on_connect(client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        client.connected_flag = True  # Set the custom flag to True when connected

    client.on_connect = on_connect
    client.connect(BROKER, PORT, 60)
    client.loop_start()  # Start the loop in a separate thread
    return client

def test_mqtt_connection(mqtt_client):
    # Wait for the connection to be established with retries
    start_time = time.time()
    attempts = 0

    while attempts < RETRIES:
        if mqtt_client.connected_flag:
            # Ensure the client has connected
            assert mqtt_client.connected_flag == True
            mqtt_client.loop_stop()  # Stop the loop after the test is done
            return  # Exit the test if connected successfully
        elif time.time() - start_time > TIMEOUT:
            # Timeout reached, try again
            attempts += 1
            print(f"Retrying... attempt {attempts}/{RETRIES}")
            time.sleep(2)  # Wait before retrying

    # If the client is still not connected after retries, fail the test
    pytest.fail("Connection to MQTT broker timed out after multiple attempts")

def test_mqtt_publish_subscribe(mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received message: {msg.payload.decode()}")
        # Ensure the received message matches the published one
        assert msg.payload.decode() == "Test message", f"Expected 'Test message', but got '{msg.payload.decode()}'"

    mqtt_client.on_message = on_message
    mqtt_client.subscribe(unique_topic)  # Subscribe to the unique topic

    # Ensure the message is received correctly
    mqtt_client.loop_start()
    mqtt_client.publish(unique_topic, "Test message", qos=1)  # Publish to the unique topic
    mqtt_client.loop_stop()
