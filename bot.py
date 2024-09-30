import win32gui
import win32api
import win32con
import time


child_handles = []

#Mute sound
def sound_off(): 
    lParam = win32api.MAKELONG(35, 450)
    win32api.SendMessage(child_handles[-3], win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32api.SendMessage(child_handles[-3], win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)

#Finder telegram id
def hwnd_finder():
    hWnd = win32gui.FindWindow(None, "TelegramDesktop")
    return hWnd

#Finder telegram app
def all_ok(hwnd, param):
    child_handles.append(hwnd)

#Clicker
def clicker(x,y):
    lParam = win32api.MAKELONG(x, y) #position of the clicker
    
    win32api.SendMessage(child_handles[-3], win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32api.SendMessage(child_handles[-3], win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)
    time.sleep(0.01)


win32gui.EnumChildWindows(hwnd_finder(), all_ok, None)

sound_off()

while True:
    clicker(190,345)