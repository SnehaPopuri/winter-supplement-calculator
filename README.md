# Winter Supplement Calculator

The Winter Supplement Calculator is a web-based application that calculates eligibility for winter supplement benefits based on user inputs. It uses MQTT for communication between the frontend and backend, enabling real-time interactions.

## Features

- **Frontend**: A clean web-based interface.
- **Backend**: Python-powered MQTT engine for eligibility calculations.
- **Real-time Communication**: Communicates via MQTT for live results.
- **Scalable**: Can be extended with additional calculations or logic.

## Setup Instructions
### Prerequisites

- Python 3.x installed on your machine.
- A modern web browser to load the frontend.
- Access to a public MQTT broker (e.g., test.mosquitto.org).

### 1. Clone the Repository
```bash
git clone https://github.com/SnehaPopuri/winter-supplement-calculator.git
cd winter-supplement-calculator
```
### 2. Install Backend Dependencies

```bash
pip install -r requirements.txt
```
### 3. Run the Frontend
- Open `index.html` in your browser, or serve it locally:
```bash
python -m http.server 8000
```
Access it at http://localhost:8000
- Enter username: `user`, password: `password` to login.
```bash
python main.py
```
### 4. Update the MQTT Topic ID (Local Setup)

If you want to run the application on your local machine and change the MQTT topic ID:
Copy the Topic id from the frontend and paste into backend system. Or for manual setup:

- **Backend (`main.py`)**:  
  Open `main.py` and locate the following constants for the input and output topics. Change them to your desired topic IDs:
  ```python
  TOPIC_INPUT = "your_custom_topic/input/"
  TOPIC_OUTPUT = "your_custom_topic/output/"
  ```
- **Frontend (`index.html`)**:  
  Open `index.html` and locate the JavaScript section where the topic ID is generated. You can replace `crypto.randomUUID()` with a static ID or leave it as is to generate a new ID each time the page is loaded:
  ```javascript
  const uniqueId = crypto.randomUUID(); // Or set a custom ID
  document.getElementById('mqttTopicId').value = uniqueId;
  ```
##You can also check the results of MQTT in cloud by setting up 
   ```javascript
   website: "https://testclient-cloud.mqtt.cool"
   Choose: "tcp://test.mosquitto.org:1883"
   Enter the "SUBSCRIBER IDs".
   ```
  Here you have two IDS: 
  - Input ``BRE/calculateWinterSupplementInput/14a8301b-5999-47cf-914e-a604d82e218b``
  - Output ``BRE/calculateWinterSupplementOutput/14a8301b-5999-47cf-914e-a604d82e218b``

### Demo Video
[Download Demo Video](./demo.mp4)

## Troubleshooting

### MQTT Connection Issues:
- Ensure the broker (`test.mosquitto.org`) is reachable.
- Verify the topic IDs match between the frontend and backend.
- If you are using a custom broker, make sure the server address and port are correctly configured.

### Frontend Not Displaying Results:
- Check the browser console for errors.
- Verify the backend is running and properly connected to the broker.



## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
