# import the necessary packages

import argparse
import sys
import zmq

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--server-port", required=True, type=str, help="server's port")
ap.add_argument("-i", "--server-ip", required=True, type=str, help="server's ip address")
args = vars(ap.parse_args())

context = zmq.Context()

print("[INFO] connecting to the server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://{}:{}".format(args["server_ip"], args["server_port"]))

while True:
  message = input("[INPUT] What is the best type of pie? ")
  print("[INFO] sending '{}'".format(message))
  socket.send(message.encode("ascii"))

  response = socket.recv().decode("ascii")
  print("[INFO] received reply '{}'".format(response))

  if response == "quitting server...":
    print("[INFO] the server is shutting down, so exiting the client")
    sys.exit(0)
