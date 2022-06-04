import random
import pyautogui as pg
import time
animal = ('You are monkey', 'You are a Gorilla')
time.sleep(8)
for i in range(500):
a = random.choice(animal)
pg.write("Hello Friend " + a)
pg.press('enter')
