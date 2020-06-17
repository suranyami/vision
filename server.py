from imagezmq import imagezmq
import imutils
import cv2
import argparse
import sys
import zmq

imageHub = imagezmq.ImageHub()

while True:
  (rpiName, frame) = imageHub.recv_image()
  imageHub.send_reply(b'OK')
  print("[INFO] receiving data from {}...".format(rpiName))

  frame = imutils.resize(frame, width=400)

  cv2.putText(frame, rpiName, (10, 25),
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
  
  cv2.imshow(rpiName, frame)
  key = cv2.waitKey(1) & 0xFF

  if key == ord("q"):
    break

cvs.destroyAllWindows()

