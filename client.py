# import the necessary packages
from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--server-ip", required=True, type=str,
  help="ip address of the server to which the client will connect")
ap.add_argument("-p", "--server-port", required=True,
  type=str, help="server's port")
args = vars(ap.parse_args())

# initialize the ImageSender object with the socket address of the server
sender = imagezmq.ImageSender(
  connect_to="tcp://{}:{}".format(args["server_ip"], args["server_port"]))

rpiName = socket.gethostname()

vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

while True:
  # read the frame from the camera and send it to the server
  frame = vs.read()
  sender.send_image(rpiName, frame)
