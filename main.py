import pyautogui
import time
import keyboard
import win32api


def click(x, y):
    win32api.SetCursorPos(x, y)
    win32api.mouse_event(win32api.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.001)
    win32api.mousr_event(win32api.MOUSEEVENTF_LEFTUP, 0, 0)


if __name__ == '__main__':
    while keyboard.is_pressed('a') == False:
        if pyautogui.pixel(760, 700)[1] == 0:
            click(760, 700)
        if pyautogui.pixel(790, 700)[1] == 0:
            click(790, 700)
        if pyautogui.pixel(820, 700)[1] == 0:
            click(820, 700)
        if pyautogui.pixel(860, 700)[1] == 0:
            click(860, 700)
