import paho.mqtt.client as mqtt
import json
from rules_engine import determine_eligibility

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC_INPUT = "BRE/calculateWinterSupplementInput/"
TOPIC_OUTPUT = "BRE/calculateWinterSupplementOutput/"

def on_message(client, userdata, msg, properties=None):
    """
    Callback for when a message is received on a subscribed topic.
    """
    print(msg.topic+" "+str(msg.payload))
    print(f"Received message on {msg.topic}: {msg.payload.decode()}")
    input_data = json.loads(msg.payload.decode())
    output_data = determine_eligibility(input_data)
    output_topic = TOPIC_OUTPUT + input_data["id"]
    client.publish(output_topic, json.dumps(output_data))
    print(f"Published result to {output_topic}: {output_data}")

def on_connect(client, userdata, flags, rc, properties=None):
    # Updated callback signature
    print("Connected with result code "+str(rc))

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)
    print("Connected to MQTT broker")

    topic_id = input("Enter the MQTT topic ID: ")
    input_topic = TOPIC_INPUT + topic_id
    client.subscribe(input_topic)
    print(f"Subscribed to topic: {input_topic}")

    client.loop_forever()

if __name__ == "__main__":
    main()