import cv2 
import numpy as np
from PIL import Image

INPUT = '../Videos/WaveStock.mp4' #Webcam number or filepath to video
IMG_TEMP_PATH = '~tmp.png'

capture = cv2.VideoCapture(INPUT)

#capture.open()
print(capture.isOpened())

while capture.isOpened():
	# Capture frame-by-frame
	ret, frame = capture.read()
	
	# Operate on the frame
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# Save the new frame as a temp file
	cv2.imwrite(IMG_TEMP_PATH, frame)
	
	# Load the image with PIL for further processing
	pFrame = Image.open(IMG_TEMP_PATH)
	#pFrame.size(240, 240)
	
	# Display the new frame
	cv2.imshow('frame', gray) # THIS DOES NOT WORK ON SYSTEMS WITH KDE AS THE ENVIRONMENT
	
	if cv2.waitKey(0) & 0xFF == ord('q'):
		break

# Loop completed, release the capture
capture.release()
cv2.destroyAllWindows()

