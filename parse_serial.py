#!/usr/bin/env python3
from typing import Container

import serial
from crsf_parser import CRSFParser, PacketValidationStatus
from crsf_parser.frames import SYNC_BYTE_BIN_STRING
from crsf_parser.handling import crsf_build_frame
from crsf_parser.payloads import PacketsTypes


def print_frame(frame: Container, status: PacketValidationStatus) -> None:
    print(
        f"""
    {status}
    {frame}
    """
    )


print("UART Demonstration Program")
print("NVIDIA Jetson Nano Developer Kit")

crsf_parser = CRSFParser(print_frame)
n = 10
v = 1
with serial.Serial(
        "/dev/ttyTHS1",
        115200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE) as ser:
    input = bytearray()
    while True:
        # if n == 0:
        #     n = 10
        #     frame = crsf_build_frame(
        #         PacketsTypes.BATTERY_SENSOR,
        #         {"voltage": v, "current": 1, "capacity": 100, "remaining": 100},
        #     )
        #     v += 1
        #     # ser.write(frame)
        # n = n - 1
        if ser.in_waiting == 0:
            print("No data")
            continue

        byte = ser.read()
        if byte == SYNC_BYTE_BIN_STRING:
            print("SYNC_BYTE")
            input.clear()

        # values = ser.read(100)
        # input.extend(values)

        # print(input)
        # crsf_parser.parse_stream(input)
