import json
import time
from datetime import datetime
import uuid
import socket

class PhysicalLayer:
    def send(self, data):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 📡 Physical Layer: Converting data to binary stream")
        try:
            bits = ''.join(format(ord(char), '08b') for char in data)
            print(f"[{timestamp}] ✓ Physical Layer: Successfully converted {len(bits)} bits")
            return bits
        except Exception as e:
            print(f"[{timestamp}] ❌ Physical Layer Error: Failed to convert data - {str(e)}")
            raise

    def receive(self, bits):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 📡 Physical Layer: Receiving binary stream")
        try:
            chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
            print(f"[{timestamp}] ✓ Physical Layer: Successfully decoded {len(chars)} characters")
            return ''.join(chars)
        except Exception as e:
            print(f"[{timestamp}] ❌ Physical Layer Error: Failed to decode bits - {str(e)}")
            raise


class DataLinkLayer:
    def send(self, bits, mac_address):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 🔗 Data Link Layer: Creating frame")
        frame = {
            'MAC_source': mac_address,
            'MAC_dest': 'FF:FF:FF:FF:FF:FF',
            'Data': bits,
            'CRC': hash(bits) % 100000,
            'timestamp': time.time()
        }
        print(f"[{timestamp}] ✓ Data Link Layer: Frame created with CRC: {frame['CRC']}")
        return frame

    def receive(self, frame):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 🔗 Data Link Layer: Processing frame from {frame['MAC_source']}")
        return frame['Data']


class NetworkLayer:
    def send(self, frame, ip_address):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 🌐 Network Layer: Creating IP packet")
        packet = {
            'version': 4,
            'source_ip': ip_address,
            'dest_ip': '192.168.1.1',
            'ttl': 64,
            'protocol': 'TCP',
            'payload': frame,
            'timestamp': time.time()
        }
        print(f"[{timestamp}] ✓ Network Layer: Packet created with TTL: {packet['ttl']}")
        return packet

    def receive(self, packet):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 🌐 Network Layer: Processing packet from {packet['source_ip']}")
        return packet['payload']


class TransportLayer:
    def send(self, packet, seq_num):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 🚢 Transport Layer: Creating TCP segment")
        segment = {
            'source_port': 12345,
            'dest_port': 80,
            'sequence': seq_num,
            'ack_number': 0,
            'window_size': 64240,
            'data': packet,
            'timestamp': time.time()
        }
        print(f"[{timestamp}] ✓ Transport Layer: Segment created with seq: {seq_num}")
        return segment

    def receive(self, segment):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 🚢 Transport Layer: Processing segment #{segment['sequence']}")
        return segment['data']


class SessionLayer:
    def send(self, segment, session_id):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 🔄 Session Layer: Establishing session")
        session = {
            'session_id': session_id,
            'created_at': time.time(),
            'status': 'active',
            'data': segment,
            'checksum': hash(str(segment)) % 100000
        }
        print(f"[{timestamp}] ✓ Session Layer: Session established: {session_id}")
        return session

    def receive(self, session):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 🔄 Session Layer: Validating session {session['session_id']}")
        return session['data']


class PresentationLayer:
    def send(self, session):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 🔠 Presentation Layer: Encoding and compressing data")
        try:
            encoded = json.dumps(session)
            print(f"[{timestamp}] ✓ Presentation Layer: Data encoded successfully")
            return encoded
        except Exception as e:
            print(f"[{timestamp}] ❌ Presentation Layer Error: Encoding failed - {str(e)}")
            raise

    def receive(self, encoded):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 🔠 Presentation Layer: Decoding data")
        try:
            session = json.loads(encoded)
            print(f"[{timestamp}] ✓ Presentation Layer: Data decoded successfully")
            return session
        except json.JSONDecodeError as e:
            print(f"[{timestamp}] ❌ Presentation Layer Error: Decoding failed - {str(e)}")
            raise


class ApplicationLayer:
    def send(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 💻 Application Layer: Creating application data")
        request = {
            'protocol': 'HTTP/1.1',
            'method': 'POST',
            'content_type': 'text/plain',
            'content_length': len(message),
            'body': message,
            'timestamp': time.time()
        }
        print(f"[{timestamp}] ✓ Application Layer: Request created")
        return request

    def receive(self, request):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] 💻 Application Layer: Processing {request['protocol']} request")
        return request['body']


if __name__ == "__main__":
    email_content = "Subject: Meeting Update\nHi team, the project meeting is scheduled for tomorrow at 2 PM."
    
    device_mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                          for elements in range(0,8*6,8)][::-1])
    
    hostname = socket.gethostname()
    sender_ip = socket.gethostbyname(hostname)
    
    packet_sequence = 42
    email_session = "EMAIL_SESSION_789"

    application_layer = ApplicationLayer()
    presentation_layer = PresentationLayer()
    session_layer = SessionLayer()
    transport_layer = TransportLayer()
    network_layer = NetworkLayer()
    datalink_layer = DataLinkLayer()
    physical_layer = PhysicalLayer()

    print("\n=== Starting Email Transmission Through OSI Layers ===\n")

    print("--- Encapsulation Process Starting ---")
    application_payload = application_layer.send(email_content)
    encoded_payload = presentation_layer.send(application_payload)
    session_payload = session_layer.send(encoded_payload, email_session)
    transport_segment = transport_layer.send(session_payload, packet_sequence)
    network_packet = network_layer.send(transport_segment, sender_ip)
    datalink_frame = datalink_layer.send(json.dumps(network_packet), device_mac)
    transmitted_bits = physical_layer.send(json.dumps(datalink_frame))

    print("\n=== Data Successfully Encapsulated and Transmitted ===\n")

    print("--- Decapsulation Process Starting ---")
    received_binary = physical_layer.receive(transmitted_bits)
    decoded_frame = json.loads(received_binary)
    extracted_packet_data = datalink_layer.receive(decoded_frame)
    decoded_packet = json.loads(extracted_packet_data)
    extracted_segment = network_layer.receive(decoded_packet)
    extracted_session_data = transport_layer.receive(extracted_segment)
    extracted_payload = session_layer.receive(extracted_session_data)
    decoded_content = presentation_layer.receive(extracted_payload)
    final_message = application_layer.receive(decoded_content)

    print("\n=== Final Received Message ===")
    print("Email Content:", final_message)
    print("\n=== Email Transmission Complete ===")
