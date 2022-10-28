import pyautogui  
import time

digite = input("Mensagem de boot: ")
mensagem = digite
n = 40 
time.sleep(2)

for i in range(n):
    pyautogui.typewrite(mensagem + "\n")