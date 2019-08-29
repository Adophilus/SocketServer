# SocketServer
A simple socket server class for python

Usage
-----

```
# main.py script

from SocketServer import SocketServer

def onConnect (client, err):
	if err:
		print("An error occurred!");
	else:
		print("Received new connection from %s" % client["ip"]);

def onSend (data, client, err):
	if err:
		print("An error occurred!");
	else:
		print("Sent data to %s" % client["ip"]);

def onReceive (data, client, err):
	if err:
		print("An error occurred!");
	else:
		print("Received data from %s" % client["ip"]);

# Initiate the server
server = SocketServer(host = "localhost", port = 8080, allowMultipleConnections = True, maxConnections = 2);

# define the callbacks
server.onConnect(onConnect);
server.onSend(onSend);
server.onRecv(onReceive);

# Start the server
server.start();

# Wait for clients
aClient = server.waitForConnections();
server.receive(aClient, _async = True);
server.send(aClient, "Welcome!");
```
