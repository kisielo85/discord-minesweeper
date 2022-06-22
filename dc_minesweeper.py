from time import sleep
import requests
from random import randrange
import os

token = "discord_token_here"

width,height=7,5
mines=5

num=["⓪","①","②","③","④","⑤","⑥","⑦","⑧","⑨","Ⓧ"]

def minesweeper():
    def addMine(x,y):
        tab[y][x]=10
        for i in range(-1,2):
            for j in range(-1,2):
                xx=x+i
                yy=y+j
                if (xx>=0 and yy>=0 and xx<width and yy<height and tab[yy][xx]!=10):
                    tab[yy][xx]+=1 #if not out of range, and not a mine

    tab=[[0 for x in range(0,width)] for y in range(0,height)]
    for i in range(mines):
        while True:
            xx=randrange(width)
            yy=randrange(height)
            if tab[yy][xx]!=10:
                addMine(xx,yy)
                break
    
    return tab
    
def show(tab):
    consoleNum=["0","1","2","3","4","5","6","7","8","9","X"]
    for y in range(height):
        t=""
        for x in range(width):
            t+=" "+consoleNum[tab[y][x]]
        print(t)
    print()

def tabToText(tab):
    t=""
    for y in range(height):
        for x in range(width):
            t+="||"+num[tab[y][x]]+"||"
        if y==0:
            t+=" Ⓧ =☠"
        t+="\n"
    return t
            
while(1):
    if os.name == 'nt':
      os.system('cls')
    else:
      os.system('clear')
    tab=minesweeper()
    show(tab)
    t="UTC+2\n"+tabToText(tab)
    requests.patch(url="https://discord.com/api/v9/users/@me", headers= {"authorization": token}, json = {"bio": t} )
    sleep(1200)#20min
