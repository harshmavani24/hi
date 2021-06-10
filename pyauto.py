import pyautogui, time

pyautogui.write("adb shell input keyevent 61 && adb shell input keyevent 61 && adb shell input keyevent 66")
pyautogui.press('enter')
time.sleep(5)