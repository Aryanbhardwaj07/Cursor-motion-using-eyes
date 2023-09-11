# import pyautogui
# pyautogui.FAILSAFE = False
from win32.win32api import GetSystemMetrics
from pynput.mouse import Listener,Button,Controller
from time import *
mouse=Controller()
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
print(width,height)
def firstpos(x,y):
    mouse.position=(x,y)
def left_click():
    mouse.click(Button.left,1)
    time.sleep(0.5)
def right_click():
    
    mouse.click(Button.right,1)
    time.sleep(0.5)
def navigateto(x,y,current_value):
    current_value1=[]
    current_value1.append(x)
    current_value1.append(y)
    movex=0
    movey=0
    
    if((current_value1[0]-current_value[0])>=5): # this is for value of x
        movex=11
    if((current_value1[0]-current_value[0])==4):
        movex=8
    if((current_value1[0]-current_value[0])==3):
        movex=6
    if((current_value1[0]-current_value[0])==2):
        movex=2
    if((current_value1[0]-current_value[0])==1):
        movex=1
    if((current_value1[0]-current_value[0])<=-5): # this is for negative value of x
        movex=-11
    if((current_value1[0]-current_value[0])==-4):
        movex=-8
    if((current_value1[0]-current_value[0])==-3):
        movex=-6
    if((current_value1[0]-current_value[0])==-2):
        movex=-2
    if((current_value1[0]-current_value[0])==-1):
        movex=-1
        
    if((current_value1[1]-current_value[0])>=5): # this is for value of y
        movex=11
    if((current_value1[1]-current_value[1])==4):
        movex=8
    if((current_value1[1]-current_value[1])==3):
        movex=6
    if((current_value1[1]-current_value[1])==2):
        movex=2
    if((current_value1[1]-current_value[1])==1):
        movex=1

    if((current_value1[1]-current_value[0])<=-5): # this is for negative value of y
        movex=-11
    if((current_value1[1]-current_value[1])==-4):
        movex=-8
    if((current_value1[1]-current_value[1])==-3):
        movex=-6
    if((current_value1[1]-current_value[1])==-2):
        movex=-2
        
    if((current_value1[1]-current_value[1])==-1):
        movex=-1

    #mouse.move(movex,movey)
    mouse.move((current_value1[0]-current_value[0]),(current_value1[1]-current_value[1]))
    #pyautogui.moveTo((current_value1[0]-current_value[0]),(current_value1[1]-current_value[1]),duration=2,tween=pyautogui.linear)
    # print("movex:",movex)
    # print("movey:",movey)
    # print((current_value1[0]-current_value[0]),(current_value1[1]-current_value[1]))
    current_value.pop()
    current_value.pop()
    current_value.append(current_value1[0])
    current_value.append(current_value1[1])
    current_value1.pop()
    current_value1.pop()

if(width==1920):
    middlepoint1,middlepoint2=960,540
firstpos(middlepoint1,middlepoint2)