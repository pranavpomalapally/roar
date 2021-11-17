#importing websocket
from websocket import create_connection

# importing pygame module
import pygame
 
# importing sys module
import sys
 
# initialising pygame and create display
pygame.init()
display = pygame.display.set_mode((300, 300))

# create websocket connection
ws = create_connection("ws://192.168.50.228:81/control")

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
   #ws = create_connection("ws://192.168.50.228:81/control")
       
    # creating a loop to check events that are occuring
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