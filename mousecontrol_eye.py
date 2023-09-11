from win32.win32api import GetSystemMetrics
from pynput.mouse import Listener,Button,Controller
import time
class mousecontrol:
    def __init__(self):
        self.mouse=Controller()
    # print(width,height)
    def firstpos(self,x,y):
        self.mouse.position=(x,y)
    def left_click(self):
        self.mouse.click(Button.left,1)
        time.sleep(0.2)#this will reduce multiple clicks
    def right_click(self):
        self.mouse.click(Button.right,1)
        time.sleep(0.2)#this will reduce multiple clicks