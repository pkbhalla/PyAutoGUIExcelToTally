import pandas as pd
import pyautogui as pg
import time

df = pd.read_csv("Book1.csv")

pn = df["Party_name"].values
cg = df["Under"].values
amt = df["Opening balance"].values

zipped = zip(pn, cg, amt)

time.sleep(3)


pg.press("A")
time.sleep(1)
pg.press("L")
time.sleep(1)
pg.press("C")
time.sleep(1)  

for (a,b,c) in zipped:      
    pg.typewrite(a)
    pg.press("enter")
    pg.press("enter")
    pg.typewrite(b)
    pg.press("enter")
    pg.press("enter")
    pg.press("enter")
    pg.press("enter")
    pg.press("enter")
    pg.press("enter")
    pg.press("enter")
    pg.press("enter")
    pg.press("enter")
    pg.press("enter")
    pg.typewrite(str(c))
    pg.press("enter")
    pg.press("enter")
    pg.press("enter")