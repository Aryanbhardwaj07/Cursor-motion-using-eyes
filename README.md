# Cursor-motion-using-eyes

### Demo video:

https://drive.google.com/file/d/1YP1Tb87vA3N9BZ_J3T8EIHrdnYx0CDRv/view?usp=share_link

### Description 

The purpose of this application is to control cursor movements by just gazing at the screen and moving our face to drag it. <br>
This application is beneficial for the physically disabled people who cannot use their hands to work on a computer so this would help them handle mouse events easily. <br>
This might help eliminate poverty by providing jobs to such people from this eye-tracking technology with an interface of a handy computer. <br>
To make this project, I used <b> Python </b> language and <b> Opencv, Dlib, Pynput, PyQt5 </b> as Major Libraries.

### working

At interface of the cursor movement application, the user needs to input the camera number, if it is a laptop camera then the default number value is 1, if the user has attached an external camera, then the user will input number 2 as a value and if multiple cameras are attached then user needs to input the correct camera number to run the application. 
Now, After adding the camera number, the user needs to specify the aspect ratio of the camera which is used as a webcam. Most of the webcam comes with 4:3 as an aspect ratio so this application comes compatible with 4:3. But If the camera-input aspect ratio is 16:9 then the user needs to input selection in an aspect ratio checkbox. 
After choosing the correct aspect ratio, the user will check whether a camera is flipped by default. If a webcam is flipped then the user will check the inverse camera button. It will reverse the flipping and tracking will happen in exact order. After choosing correct alternatives user needs to balance out the lighting with the help of illumination slider which helps in low light conditions. 
After all this, we can see our face being recognized and the cursor will be moving on face movements. 
It will work like, If our right eye blinks intentionally then it is considered as a right click and if it blinks naturally then clicks are not considered. Same goes for the left eye. Also, the mouse cursor is moving by subtracting the distance between midpoint of face and midpoint of frame.
At last, Users can click the letter ‘Q’ to exit. By clicking ’Q’ the user just exits out of the OpenCV video frame. To exit the full program, users need to close the interface too. 
It solves problems like how we can control the cursor motion without the manual interaction and hence it is beneficial for the people who are physically disabled as they can use their eyes to communicate with the computers and probably will not be dependent on anyone. So it will eliminate poverty by providing jobs to such people from this eye-tracking technology.
There are many pros of using this as in this application, Users can use it in-game for many game functions. Camera input can be changed. Users can set illumination in video screens according to their background illumination. It is easy to control and one can change aspect ratio settings as well.
Now talking about the future scope, the user interface can be made more handy and attractive over time. Like we can add different functions for different eye and face gestures and will help increase the research in this field. Game functions can be made more advanced. In the upcoming updates, any individual in distress can be helped with communication to a far greater extent.

#### To run the project, install the following dependencies:

1. cmake==3.18.4.post1
2. dlib==19.21.1
3. numpy==1.20.1
4. opencv-python==4.5.1.48
5. pynput==1.7.2
6. PyQt5==5.15.2
7. PyQt5-sip==12.8.1
8. PyQt5-stubs==5.14.2.2
9. pywin32==300
10. six==1.15.0



