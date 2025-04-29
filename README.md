# Web-Based Light Scheduler (IoT Project)

This project simulates a real-world IoT dashboard to **schedule a light** using a graphical web interface, WebSocket server, and MQTT communication.

---

## Project Structure

- **frontend/** → `index.html` — user-friendly scheduler web app (choose ON and OFF times)
- **backend/** → `server.py` — WebSocket server receiving schedules and forwarding to MQTT broker
- **subscriber/** → `subscriber.py` — MQTT subscriber that controls Arduino via serial communication

---

## How to Run the Project

### Requirements:
- Python 3.12
- `websockets`, `paho-mqtt`, `pyserial` libraries
- Mosquitto MQTT broker installed
- Arduino connected via USB

### Install Python dependencies:
```bash
pip install websockets paho-mqtt pyserial
Step-by-Step:
Start Mosquitto Broker:
"C:/Program Files/mosquitto/mosquitto.exe"
Run the WebSocket server:

Arduino will turn relay ON or OFF at scheduled times.

WebApp	Terminal Logs	Arduino Reaction

Name: TURINUMUGISHA Gasore Corene
School: Rwanda Coding Academy
Year: 2B

Instructor: Mr. Gabriel Baziramwabo

✅ Full system tested and working!
