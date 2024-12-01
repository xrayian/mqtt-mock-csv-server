# Flight Data Telemetry MQTT Publisher

This Python script is designed to send flight telemetry data from a CSV file to an MQTT broker. It uses the [Paho MQTT](https://pypi.org/project/paho-mqtt/) library to connect to the MQTT broker and publish data.

## Features

- Connects to an MQTT broker.
- Reads flight telemetry data from a CSV file.
- Publishes each row of the data (excluding the header) to a specified MQTT topic.
- Configurable broker URL, port, topic, and data file via command-line arguments.

---

## Requirements

- Python 3.11 or higher
- Libraries: Install dependencies using the following command:
  ```bash
  pip install paho-mqtt
  ```

---

## Command-Line Arguments

The script supports the following command-line arguments:

| Argument            | Description                               | Default Value                |
|---------------------|-------------------------------------------|------------------------------|
| `-b`, `--broker`    | MQTT broker URL                          | `mqtt.eclipseprojects.io`   |
| `-p`, `--port`      | MQTT broker port                         | `1883`                      |
| `-t`, `--topic`     | MQTT topic to publish data to            | `telemetry/data`            |
| `-f`, `--file`      | CSV file containing flight telemetry data| **Required**                |

---

## Usage

### Example Command

```bash
python main.py -b mqtt.eclipseprojects.io -p 1883 -t telemetry/data -f flightdata.csv
```

### Parameters:

- **Broker URL (`-b`)**: The MQTT broker's address. Default is `mqtt.eclipseprojects.io`.
- **Port (`-p`)**: The MQTT broker's port. Default is `1883`.
- **Topic (`-t`)**: The topic to which data is published. Default is `telemetry/data`.
- **File (`-f`)**: Path to the CSV file containing flight telemetry data (required).

---

## CSV File Format

- The CSV file must have a header row, which is ignored when publishing data.
- Each row should contain telemetry data separated by commas.

### Example:

```csv
TEAM_ID,MISSION_TIME,PACKET_COUNT,MODE,STATE,ALTITUDE,AIR_SPEED,HS_DEPLOYED,PC_DEPLOYED,TEMPERATURE,VOLTAGE,PRESSURE,GPS_ALTITUDE,GPS_LATITUDE,GPS_LONGITUDE,GPS_SATS,TILT_X,TILT_Y,ROT_Z,LAST_CMD
2043,1419,216,F,LAUNCH_WAIT,234.63,10.21,N,N,33.55,4.99,985.38,5.40,23.801393,90.437256,4,31,-12,0,CX/ON
...
```
---

## How It Works

1. The script establishes a connection to the MQTT broker using the provided or default settings.
2. It reads the telemetry data from the specified CSV file.
3. Each row of data (after the header) is published to the given MQTT topic.
4. A confirmation message is printed for each published row, along with the topic name.

---

## Error Handling

- If the connection to the MQTT broker fails, the script prints an error message with the return code.
- If the message fails to publish, an error message is displayed.
- If the file name is not provided, the script exits with an error message.

---

## License

This script is open-source and can be modified or redistributed under the terms of the MIT License. 

---

Feel free to contribute to this project by suggesting enhancements or reporting bugs!