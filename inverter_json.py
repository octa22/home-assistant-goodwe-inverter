"""Simple test script to check inverter UDP protocol communication"""
import asyncio
import logging
import sys

import custom_components.goodwe.goodwe_inverter as inverter

logging.basicConfig(
    format="%(asctime)-15s %(funcName)s(%(lineno)d) - %(levelname)s: %(message)s",
    stream=sys.stderr,
    level=getattr(logging, "ERROR", None),
)

# Set the appropriate IP address
IP_ADDRESS = "192.168.1.14"

inverter = asyncio.run(inverter.discover(IP_ADDRESS, 8899))
response = asyncio.run(inverter.read_runtime_data())

comma = 0
output = "{"
for (sensor, _, _, _, _, _) in inverter.sensors():
    if (comma):
        output += ","
    else:
        comma = 1
    output += "'" + sensor + "':'" + str(response[sensor]) + "'"
output += "}"
print(output)

