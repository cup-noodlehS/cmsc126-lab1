import json

class PhysicalLayer:
    def send(self, data):
        print("[Physical Layer] Sending data as bits")
        bits = ''.join(format(ord(char), '08b') for char in data)
        return bits

    def receive(self, bits):
        print("[Physical Layer] Receiving data from bits")
        chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
        return ''.join(chars)


class DataLinkLayer:
    def send(self, bits, mac_address):
        print("[Data Link Layer] Creating frame with MAC address")
        frame = {'MAC': mac_address, 'Data': bits}
        return frame

    def receive(self, frame):
        print("[Data Link Layer] Extracting data from frame")
        return frame['Data']


class NetworkLayer:
    def send(self, frame, ip_address):
        print("[Network Layer] Creating packet with IP address")
        packet = {'IP': ip_address, 'Frame': frame}
        return packet

    def receive(self, packet):
        print("[Network Layer] Extracting frame from packet")
        return packet['Frame']


class TransportLayer:
    def send(self, packet, seq_num):
        print("[Transport Layer] Adding sequence number")
        segment = {'Seq': seq_num, 'Packet': packet}
        return segment

    def receive(self, segment):
        print("[Transport Layer] Extracting packet from segment")
        return segment['Packet']


class SessionLayer:
    def send(self, segment, session_id):
        print("[Session Layer] Managing session with ID")
        session = {'SessionID': session_id, 'Segment': segment}
        return session

    def receive(self, session):
        print("[Session Layer] Extracting segment from session")
        return session['Segment']


class PresentationLayer:
    def send(self, session):
        print("[Presentation Layer] Encoding session data")
        encoded = json.dumps(session)
        return encoded

    def receive(self, encoded):
        print("[Presentation Layer] Decoding session data")
        session = json.loads(encoded)
        return session


class ApplicationLayer:
    def send(self, message):
        print("[Application Layer] Creating HTTP-like request")
        request = {'HTTP_Request': message}
        return request

    def receive(self, request):
        print("[Application Layer] Extracting message from request")
        return request['HTTP_Request']


if __name__ == "__main__":
    message = "Hello, OSI Model!"
    mac_address = "00:1B:44:11:3A:B7"
    ip_address = "192.168.1.1"
    seq_num = 1
    session_id = "12345"

    # Instantiate each layer
    app = ApplicationLayer()
    pres = PresentationLayer()
    sess = SessionLayer()
    trans = TransportLayer()
    net = NetworkLayer()
    data_link = DataLinkLayer()
    phys = PhysicalLayer()

    print("Starting OSI Model Simulation...")

    # Sending
    app_data = app.send(message)
    pres_data = pres.send(app_data)
    sess_data = sess.send(pres_data, session_id)
    trans_data = trans.send(sess_data, seq_num)
    net_data = net.send(trans_data, ip_address)
    link_data = data_link.send(json.dumps(net_data), mac_address)
    phys_data = phys.send(json.dumps(link_data))

    print("\n--- Data Sent ---\n")

    # Receiving
    received_bits = phys.receive(phys_data)
    received_frame = json.loads(received_bits)
    received_link_data = data_link.receive(received_frame)
    received_packet = json.loads(received_link_data)
    received_segment = net.receive(received_packet)
    received_session = trans.receive(received_segment)
    received_pres = sess.receive(received_session)
    received_app = pres.receive(received_pres)
    received_message = app.receive(received_app)


    print("\n--- Data Received ---\n")
    print("Received message:", received_message)
    print("OSI Model Simulation Complete!")
