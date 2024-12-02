import paho.mqtt.client as mqtt
import json
from rules_engine import determine_eligibility

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC_INPUT = "BRE/calculateWinterSupplementInput/"
TOPIC_OUTPUT = "BRE/calculateWinterSupplementOutput/"

def save_to_json(id, result):
    """
    Save the result to a JSON file.
    """
    filename = f"result_{id}.json"
    try:
        with open(filename, 'w') as file:
            json.dump(result, file, indent=4)
        print(f"Result saved to {filename}")
    except Exception as e:
        print(f"Failed to save result to JSON: {e}")

def on_message(client, userdata, msg):
    """
    Callback for when a message is received on a subscribed topic.
    """
    print(f"Received message on {msg.topic}: {msg.payload.decode()}")
    input_data = json.loads(msg.payload.decode())
    
    # Process the input data using the eligibility logic
    output_data = determine_eligibility(input_data)
    
    # Save the result to a JSON file
    save_to_json(input_data["id"], output_data)
    
    # Publish the result to the output topic
    output_topic = TOPIC_OUTPUT + input_data["id"]
    client.publish(output_topic, json.dumps(output_data))
    print(f"Published result to {output_topic}: {output_data}")

def main():
    client = mqtt.Client()
    client.on_message = on_message

    # Connect to the MQTT broker
    client.connect(BROKER, PORT, 60)
    print("Connected to MQTT broker")

    # Get the topic ID from the user and subscribe to the input topic
    topic_id = input("Enter the MQTT topic ID: ")
    input_topic = TOPIC_INPUT + topic_id
    client.subscribe(input_topic)
    print(f"Subscribed to topic: {input_topic}")

    # Start the MQTT client loop to listen for messages
    client.loop_forever()

if __name__ == "__main__":
    main()
