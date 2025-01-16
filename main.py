# python 3.11

import random
import sys
import time
import argparse

from paho.mqtt import client as mqtt_client
from paho.mqtt.client import CallbackAPIVersion

global brokerURL
global brokerPort
global topic
global fileName

brokerURL = "127.0.0.1"
brokerPort = 1883
topic = "telemetry/data"
fileName = "flightdata.csv"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(CallbackAPIVersion.VERSION1,client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(brokerURL, brokerPort)
    return client


def sendFlightDataToMQTTClient(client):
    with open(fileName, "r") as file:
        data = file.readlines()
        i = 0
        for line in data:
            if (i == 0):
                i = 1  # skip header
                continue
            formattedLine = line
            formattedLine = line.replace(",", ", ")
            formattedLine = formattedLine.replace("  ", " ")
            formattedLine = formattedLine.replace("\n", "")
            result = client.publish(topic, formattedLine)
            status = result[0]
            if status == 0:
                print(f"Sent `{formattedLine}` to topic `{topic}`")
            else:
                print(f"Failed to send message to topic {topic}")
            time.sleep(1.0)

        file.close()


def publish(client):
    sendFlightDataToMQTTClient(client)


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--broker", type=str, help="Broker URL")
    parser.add_argument("-p", "--port", type=int, help="Broker Port")
    parser.add_argument("-t", "--topic", type=str, help="Specify Topic Name")
    parser.add_argument("-f", "--file", type=str, help="Specify File Name")
    args = parser.parse_args()

    if args.broker:
        brokerURL = args.broker
    if args.port:
        brokerPort = args.port
    if args.topic:
        topic = args.topic
    if args.file:
        global fileName
        fileName = args.file
    else:
        print("Please provide file name using -f or --file")
        sys.exit()

    run()


if __name__ == '__main__':
    main()
