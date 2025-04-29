import asyncio
import websockets
import json
import subprocess

async def handler(websocket):
    async for message in websocket:
        data = json.loads(message)
        on_time = data['on']
        off_time = data['off']
        print(f"Received schedule -> ON: {on_time}, OFF: {off_time}")
        # Publish ON time schedule
        subprocess.run(["C:/Program Files/Mosquitto/mosquitto_pub.exe", "-h", "localhost", "-t", "relay/schedule", "-m", f"ON:{on_time}"])

        # Publish OFF time schedule
        subprocess.run(["C:/Program Files/Mosquitto/mosquitto_pub.exe", "-h", "localhost", "-t", "relay/schedule", "-m", f"OFF:{off_time}"])


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())

# subscriber/subscriber.py
import serial
import paho.mqtt.client as mqtt

ser = serial.Serial('/dev/ttyUSB0', 9600)

# Store ON and OFF times
schedule = {"ON": None, "OFF": None}

from datetime import datetime
import time

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    if payload.startswith("ON:"):
        schedule["ON"] = payload.split(":")[1]
    elif payload.startswith("OFF:"):
        schedule["OFF"] = payload.split(":")[1]

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe("relay/schedule")
client.loop_start()

while True:
    now = datetime.now().strftime("%H:%M")
    if schedule["ON"] == now:
        ser.write(b'1')
        print("Light ON")
        time.sleep(60)
    elif schedule["OFF"] == now:
        ser.write(b'0')
        print("Light OFF")
        time.sleep(60)
    time.sleep(1)