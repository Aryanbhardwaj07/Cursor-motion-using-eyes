import cv2 as cv
cv2=cv
import dlib

cap=cv.VideoCapture("testvideo.mp4")
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
def rescaleFrame(frame,scale=0.5):
    width=int(frame.shape[1]*scale)#frame.shape[1] is width of image
    height=int(frame.shape[0]*scale)#frame.shape[0] is height of image
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
while True:
    _,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray=rescaleFrame(gray)
    frame=rescaleFrame(frame)
    faces=detector(gray)
    for face in faces:
        #print(face)
        x,y=face.left(),face.right()
        x1,y1=face.top(),face.bottom()

        cv2.rectangle(frame,(x,x1),(y,y1),(0,255,0),2)
        landmarks=predictor(gray,face)
        # x=landmarks.part(37).x
        # y=landmarks.part(37).y
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)
        # cv.circle(frame,(x,y),1,(0,255,0),1)
    cv.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break

cap.release()
cv2.destroyAllWindows()