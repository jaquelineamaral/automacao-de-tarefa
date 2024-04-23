import pyautogui
import time
import pandas
import os

time.sleep(5)
print(pyautogui.position())

diretorio_atual = os.path.dirname(__file__)

tabela = pandas.read_csv(os.path.join(diretorio_atual, '../arquivos/produtos.csv'))

item = str(tabela.loc[1, 'obs'])

print(len(item))

