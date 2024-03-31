import pyautogui
import time
import sys
import pandas
import os

# pausa a cada comando do pyautogui
pyautogui.PAUSE = 3 

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# abrir o navegador

# pyautogui.press('win')
# pyautogui.write('chrome')   
# pyautogui.press('enter')

# time.sleep(3)
# pyautogui.click(x=950, y=323) #40:45

pyautogui.press('win')
pyautogui.write('microsoft edge')
pyautogui.press('enter')
time.sleep(5)

# entrar no site
pyautogui.write(link)
pyautogui.press('enter')

# pausa maoir em comando específico - 3 segundos
time.sleep(3)

pyautogui.click(x=509, y=376)
pyautogui.write('sjaqueline987@gmail.com')

# pyautogui.click(x=491, y=478)
pyautogui.press('tab')
pyautogui.write('admin123')

pyautogui.click(x=654, y=545)
# pyautogui.press('tab')
# pyautogui.press('enter')
time.sleep(3)

# importar dados
diretorio_atual = os.path.dirname(__file__)

tabela = pandas.read_csv(os.path.join(diretorio_atual, '../arquivos/produtos.csv'))
print(tabela)

