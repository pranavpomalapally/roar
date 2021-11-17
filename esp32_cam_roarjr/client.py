from websocket import create_connection
from PIL import Image
import requests
from io import BytesIO

# import cv2

# capture = cv2.VideoCapture("http://192.168.50.228/cam.mjpeg")
# while(True):
# 	ret, frame = capture.read()
# 	cv2.imshow('livestream', frame)
# 	if cv2.waitKey(1) == ord("q"):
# 		break
# capture.release()
# cv2.destroyAllWindows()

#get picture (works slowly)
url = "http://192.168.50.228/cam-lo.jpg"
#url = "http://192.168.50.228/cam.mjpeg"

response = requests.get(url)
print("got request")
img = Image.open(BytesIO(response.content))
img.show()
print(img)


# send requests (works)
# ws = create_connection("ws://192.168.50.228:81/control")
# send = "(-200, 150, -1, -1)"
# print("Sending ", send)
# ws.send(send)
# print("Sent")
# ws.close()