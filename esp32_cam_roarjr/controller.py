#imports
from websocket import create_connection
import pygame
import sys
import urllib.request
import numpy as np
import cv2 
 
# initialising pygame and create display
pygame.init()
display = pygame.display.set_mode((300, 300))
pygame.display.set_caption("WASD Keys to control")

# create websocket connection
host = "192.168.50.228"
host = "10.0.0.66"
#ws = create_connection("ws://192.168.50.228:81/control")
ws = create_connection("ws://10.0.0.66:81/control")

# speed var
speed = "250"

# quit
def quit():
    send = "(0, 0, -1, -1)"
    ws.send(send)
    pygame.quit()
    sys.exit()
 
# creating a running loop
while True:
       
    # creating a loop to check events that are occuring
    imgResp = urllib.request.urlopen(f'http://10.0.0.66/cam-lo.jpg')
    imgNp = np.frombuffer(imgResp.read(), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    # all the opencv processing is done here

    # Look into Pygame instead of OpenCV to allow for keyboard inputs
    cv2.imshow('test', img)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
         
        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
           
            # up
            if event.key == pygame.K_w:
                print("Key W has been pressed")
                send = "({}, {}, 1, 1)".format(speed, speed)
               
            # left
            if event.key == pygame.K_a:
                print("Key A has been pressed")
                send = "({}, {}, -1, 1)".format(speed, speed)
               
            # down
            if event.key == pygame.K_s:
                print("Key S has been pressed")
                send = "({}, {}, -1, -1)".format(speed, speed)

            # right
            if event.key == pygame.K_d:
                print("Key D has been pressed")
                send = "({}, {}, 1, -1)".format(speed, speed)

            # stop
            if event.key == pygame.K_h:
                print("Key H has been pressed")
                send = "({}, {}, 1, -1)".format(0, 0)

            # quit
            if event.key == pygame.K_q:
                print("Key Q has been pressed")
                quit()

            ws.send(send)
            print("Sent")