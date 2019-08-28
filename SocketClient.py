import socket
from General import General
from Clock import Clock

class SocketClient (General):
	def __init__ (self, host = "localhost", port = 8080, _buffer = 1024):
		self.host = host;
		self.port = port;
		self.buffer = _buffer;
		self.socket = socket.socket();
		self.receiving = False
		self.connected = False

		# Callback definitions
		self.onConnectCallback = self.emptyFunction;
		self.onReceiveCallback = self.emptyFunction;
		self.onSendCallback = self.emptyFunction;

	def emptyFunction (self, *args, **kwargs):
		pass;

	def connect (self, callback):
		try:
			self.socket.connect((self.host, self.port));
			self.connected = True;
			callback(True, None);
		except Exception as e:
			callback(False, e);

	def recv (self, async = False):
		self.receive(async);

	def receive (self, async = False):
		if async:
			self.setImmediate(self.processReceivedData);
		else:
			self.processReceivedData();

	def processReceivedData (self):
		try:
			data = self.socket.recv(self._buffer).decode("utf-8");
			data = self.jsonize(data);

			self.onReceiveCallback(data, None);
		except Exception as e:
			self.onReceiveCallback(False, e);

	def send (self, data):
		try:
			data = {
				"date": "date",
				"time": "time",
				"data": data
			}

			self.socket.send(self.unjsonize(data).encode("utf-8"));

			self.onSendCallback(data, None);
		except Exception as e:
			self.onSendCallback(False, e);

	def onReceive (self, callback):
		self.onReceiveCallback = callback;

	def onSend (self, callaback):
		self.onSendCallback = callback;

	def disconnect (self):
		self.socket.close();
		
if __name__ == '__main__':
	client = SocketClient();

	def onConnect (connected, err):
		if connected:
			print("Connection successful!");
		else:
			print("Connection failed!");

	client.connect(onConnect);
	client.send("Hello server!");