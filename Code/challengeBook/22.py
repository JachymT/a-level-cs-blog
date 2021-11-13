#challenge 22, python programming booklet
#creating a 10x10 random array with colours based on position

from random import randint
from tkinter import *

GREEN = "D3"

def newRandom(m=15):
    return randint(0,m)

def newArray(n=10):
    box = [[newRandom() for i in range(n)] for j in range(n)]
    return box

def main():
    ranArr = newArray()
    
    root = Tk()
    text = Text(root)
    
    for i in range(10):
        for j in range(10):
            t=str(ranArr[i][j])

            #postion of text for the tag
            start = str(i+1) + "." + str(j*3)
            end = str(i+1) + "." + str((j+1)*3)

            #number between 0 and 99 based on the position in the array
            pos = i*10 + j

            rgbDEC = int(pos *2.5)
            rgbHEX = hex(rgbDEC).split('x')[-1]

            #to get the format #xxyyzz
            if len(rgbHEX) == 1:
                rgbHEX = "0" + rgbHEX
            colour = "#" + rgbHEX + GREEN + rgbHEX
            
            if len(t) > 1:
                space = " "
            else:
                space = "  "
                
            text.insert(END, t + space)
            text.tag_add("current"+str(pos), start, end)
            text.tag_config("current"+str(pos), background=colour)
            
        text.insert(END, "\n")
        
    text.pack()
    root.geometry("300x200")
    root.mainloop()

if __name__ == "__main__":
    main()
    
