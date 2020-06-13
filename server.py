import argparse
import sys
import zmq

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--server-port",  required=True, type=str, help="server's port")
args = vars(ap.parse_args())

# create a container for all sockets in this process
context = zmq.Context()

# establish a socket for incoming connections
print("[INFO] creating socket...")
socket = context.socket(zmq.REP)
socket.bind("tcp://*:{}".format(args["server_port"]))

while True:
  # receive a message, decode it, and convert to lowercase
  message = socket.recv().decode("ascii").lower()
  print("[INFO] received message `{}`".format(message))

  # check if the correct message, *raspberry*, is received and then
  # send return message message accordingly
  if "raspberry" in message:
    print("[INFO] correct message, so sending 'correct'")
    returnMessage = "correct"
    socket.send(returnMessage.encode("ascii"))
  elif message == "quit":
    returnMessage = "quitting server..."
    socket.send(returnMessage.encode("ascii"))
    print("[INFO] terminating the server")
    sys.exit(0)
  else:
    print("[INFO] incorrect message, so requesting again")
    returnMessage = "try again!"
    socket.send(returnMessage.encode("ascii"))

