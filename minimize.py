import pyautogui
import pygetwindow

def all_down():
    windows=pyautogui.getAllTitles()
    for i in windows:
            pyautogui.getWindowsWithTitle("{}".format(i))[0].minimize()



def maximize_java():
        window = pyautogui.getAllTitles()
        for i in window:
            for j in (i.split('.')):
                if j == "java":
                    pyautogui.getWindowsWithTitle(i)[0].maximize()

def minimize_java():
        window = pyautogui.getAllTitles()
        for i in window:
            for j in (i.split('.')):
                if j == "java":
                    pyautogui.getWindowsWithTitle(i)[0].minimize()

