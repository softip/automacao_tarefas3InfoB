import pyautogui
import time

def preencher(atleta, modalidade, medalha, comite):
    campoAtleta = pyautogui.locateCenterOnScreen("aula10/atleta.png", grayscale=True, confidence=0.9)
    pyautogui.click(campoAtleta, duration=0.7)
    pyautogui.write(atleta)

    campoModalidade = pyautogui.locateCenterOnScreen("aula10/modalidade.png", grayscale=True, confidence=0.9)
    pyautogui.click(campoModalidade, duration=0.7)
    pyautogui.write(modalidade)

    campoMedalha = pyautogui.locateCenterOnScreen("aula10/medalha.png", grayscale=True, confidence=0.9)
    pyautogui.click(campoMedalha, duration=0.7)
    pyautogui.write(medalha)

    pyautogui.scroll(-300)
    time.sleep(1)

    campoComite = pyautogui.locateCenterOnScreen("aula10/comite.png", grayscale=True, confidence=0.9)
    pyautogui.click(campoComite, duration=0.7)
    pyautogui.write(comite)

    campoEnviar = pyautogui.locateCenterOnScreen("aula10/enviar.png", grayscale=True, confidence=0.9)
    pyautogui.click(campoEnviar, duration=0.7)

    time.sleep(1)
    campoOutra = pyautogui.locateCenterOnScreen("aula10/outra.png", grayscale=True, confidence=0.9)
    pyautogui.click(campoOutra, duration=0.7)

    time.sleep(1)