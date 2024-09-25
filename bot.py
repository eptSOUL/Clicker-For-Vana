import win32gui
import win32api
import win32con
import time
#import pyautogui

child_handles = []

def hwnd_finder():

    hWnd = win32gui.FindWindow(None, "TelegramDesktop")
    return hWnd

def hwnd_finder_child(hwnd, param):
    child_handles.append(hwnd)

def click(x,y):

    lParam = win32api.MAKELONG(x, y)
    #клик
    win32api.SendMessage(child_handles[-3], win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32api.SendMessage(child_handles[-3], win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)
    time.sleep(0.01)


win32gui.EnumChildWindows(hwnd_finder(), hwnd_finder_child, None)

while True:
    click(190,345)