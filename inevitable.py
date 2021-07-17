from playsound import playsound
import pyautogui
def iam_inevitable():
    playsound(r'C:\Users\DELL\Downloads\iamainevitablethanos.mp3')
    playsound(r'C:\Users\DELL\Downloads\thanos_snap.mp3')
    windows=pyautogui.getAllTitles()
    print(windows)
    for i in windows:
        pyautogui.getWindowsWithTitle("{}".format(i))[0].close()