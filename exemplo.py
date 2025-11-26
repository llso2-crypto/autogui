import pyautoguig
import time

pyautogui.FAILSAFE = True

# Aguarda o usuário preparar o ambiente
time.sleep(3)

# - Ativar janela do navegador
pyautogui.click(200, 200)   # clique em uma área do navegador

#  Digitar a URL
pyautogui.hotkey("ctrl", "l")   # seleciona barra de endereço
time.sleep(0.5)
pyautogui.write("https://www.wikipedia.org")
pyautogui.press("enter")

# Aguarda carregamento
time.sleep(3)

# Digitar termo pesquisado
pyautogui.write("Inteligência Artificial")
pyautogui.press("enter")

#  Clicar no campo de pesquisa da Wikipedia
pyautogui.click(600, 350)  # ajuste se necessário

# Aguarda carregar
time.sleep(3)

# Screenshot
screenshot = pyautogui.screenshot()
screenshot.save("resultado_wikipedia.png")
print("Automação finalizada com sucesso!")
