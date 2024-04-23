import pyautogui
import time
import sys
import pandas
import os

# pausa a cada comando do pyautogui
pyautogui.PAUSE = 1 

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

pyautogui.click(x=509, y=374)
pyautogui.write('sjaqueline987@gmail.com')

pyautogui.press('tab')
pyautogui.write('admin123')

pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

# importar dados
diretorio_atual = os.path.dirname(__file__)

tabela = pandas.read_csv(os.path.join(diretorio_atual, '../arquivos/produtos.csv'))

for linha in tabela.index:
    pyautogui.click(x=552, y=237)

    for coluna in tabela.columns:
        item = tabela.loc[linha, coluna]

        if not (coluna == 'obs' and pandas.isna(item)):
            pyautogui.write(str(item))
        pyautogui.press('tab')       
    
    pyautogui.press('enter')
    pyautogui.scroll(5000)
