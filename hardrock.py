import socket
import json
import sys

class client:
    HOST = '192.168.0.107'
    PORT = 1993
    BUF_SIZE = 100

    def __init__(self):
        self._received = ""

    def connect(self, handshake):
        self._s = socket.socket()
        self._s.connect((client.HOST, client.PORT))
        self.send(handshake)
        assert(self.recv()['status'] == True)

    def send(self, obj):
        data = json.dumps(obj) + "\n"
        self._s.send(data.encode('utf-8'))

    def recv(self):
        while not "\n" in self._received:
            received = self._s.recv(client.BUF_SIZE).decode('utf-8')
            if received == "":
                raise Exception('Server shut down')
            self._received += received

        [obj, self._received] = self._received.split("\n", 1)
        return json.loads(obj)

class observer(client):
    def connect(self):
        super().connect({"message":"connect", "type":"observer"})

class player(client):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def connect(self, character, cartype):
        super().connect({"message":"connect", "type":"player", "name":self._name, "character":character, "cartype":cartype, "tracktiled":False})
        while True:
            self.dispatch()

    def dispatch(self):
        obj = self.recv()
        message = obj['message']
        del obj['message']

        try:
            getattr(self, message)(**obj)
        except AttributeError:
            print("WARN: unhandled message {}".format(message))

    def do(self, action):
        self.send({"message":"action", "type":action})

    # messages

    def action(self, type, player): pass

    def gamestate(self, time, cars, missiles, mines):
        self.time = time
        self.cars = cars
        self.missiles = missiles
        self.mines = mines
        self.tick()

    def tick(self): pass
