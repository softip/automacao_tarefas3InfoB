import pyautogui

pyautogui.moveTo(479, 438, duration=0.5)
distancia = 200

while distancia > 0:
    pyautogui.dragRel(distancia,0, duration=0.5)
    distancia = distancia - 10
    pyautogui.dragRel(0, distancia, duration=0.5)
    pyautogui.dragRel(-distancia, 0, duration=0.5)
    distancia = distancia - 10
    pyautogui.dragRel(0, -distancia, duration=0.5)
