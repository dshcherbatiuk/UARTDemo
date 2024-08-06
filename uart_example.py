#!/usr/bin/python3
import time
import serial

print("UART Demonstration Program")
print("NVIDIA Jetson Nano Developer Kit")


def bytes_to_hex(byte_data):
    return ' '.join(f'0x{byte:02x}' for byte in byte_data)


def hexdump(data, width=8):
    """Prints a hexdump of the provided data.

    Args:
        data: The bytes-like object to be dumped.
        width (optional): The number of bytes per line (default: 16).
    """

    for offset in range(0, len(data), width):
        line_data = data[offset: offset + width]

        # Hexadecimal values
        hex_values = " ".join(f"{byte:02X}" for byte in line_data)

        # Printable characters (replacing unprintable with '.')
        printable = "".join(chr(byte) if 32 <= byte < 127 else "." for byte in line_data)

        # Output with offset, hex, and printable characters
        print(f"{offset:08X}  {hex_values:<{width * 3}}  {printable}")


serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
# Wait a second to let the port initialize
time.sleep(1)

try:
    # Send a simple header
    serial_port.write("UART Demonstration Program\r\n".encode())
    serial_port.write("NVIDIA Jetson Nano Developer Kit\r\n".encode())
    byte_buffer = []
    while True:
        if serial_port.inWaiting() > 0:
            byte = serial_port.read()
            byte_buffer.append(bytes_to_hex(byte))
            # byte_buffer.append(byte)

            if len(byte_buffer) == 8:
                # hex_value = bytes(byte_buffer).hex().upper()
                print(byte_buffer)
                # print(hexdump(byte_buffer))
                byte_buffer.clear()

            # serial_port.write(data)
            # if we get a carriage return, add a line feed too
            # \r is a carriage return; \n is a line feed
            # This is to help the tty program on the other end 
            # Windows is \r\n for carriage return, line feed
            # Macintosh and Linux use \n
            # if data == "\r".encode():
            # For Windows boxen on the other end
            # serial_port.write("\n".encode())


except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass
