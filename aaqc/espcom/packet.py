# from serial import Serial

# instructions
drone_instructions = {
    "forward": 0x01,
    "backward": 0x02,
    "left": 0x03,
    "right": 0x04,
    "increase_altitude": 0x05,
    "decrease_altitude": 0x06,
    "stop": 0x07,
    "takeoff": 0x08,
    "land": 0x09,
    "emergency": 0x0A,
    "turn_left": 0x0B,
    "turn_right": 0x0C,
    "inizialize": 0x0D,
}


def xor_checksum(packet: bytearray) -> int:
    checksum = 0
    for byte in packet:
        checksum ^= byte
    return checksum


def compose_packet(opcode: str, data: list = []) -> bytearray:
    packet = bytearray([])

    # Data length
    packet.append(len(data))

    # Opcode
    op = drone_instructions[opcode]
    packet.append(op)

    # Data
    for dat in data:
        packet.append(dat)

    # Checksum
    packet.append(xor_checksum(packet))

    return packet


def parse_packet(packet: bytearray) -> dict:
    packet_dict = {
        "data_length": packet[0],
        "opcode": packet[1],
        "data": packet[2:],
        "checksum": packet[-1],
    }

    return packet_dict


if __name__ == "__main__":
    new_packet = compose_packet("forward", [0x01, 0x02, 0x03])
    print(new_packet)
    print(parse_packet(new_packet))
