
# new fps show file


from imutils.video import FPS
import argparse
import imutils
import cv2
# construct the argument parse and parse the arguments

# created a *threaded* video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from webcam...")
vs = cv2.VideoCapture(0)
fps = FPS().start()
# loop over some frames...this time using the threaded stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	_,frame = vs.read()
	frame = imutils.resize(frame, width=400)
	# check to see if the frame should be displayed to our screen
	
	cv2.imshow("Frame", frame)
	
	# update the FPS counter
	fps.update()
	if cv2.waitKey(1) & 0xFF == ord('q'):
        # self.cap.release()
		cv2.destroyAllWindows()
		break
# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# do a bit of cleanup
cv2.destroyAllWindows()