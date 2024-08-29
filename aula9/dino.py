import pyautogui

pyautogui.click(200,200,interval=0.5)
pyautogui.press('space')

while True:
    if pyautogui.pixelMatchesColor(232,430,[83,83,83],70):
        print(pyautogui.pixel(232,430))
        pyautogui.press('space')
    elif pyautogui.pixelMatchesColor(232,395,[83,83,83],70):
        print(pyautogui.pixel(232,395))
        pyautogui.press('down', interval=2)