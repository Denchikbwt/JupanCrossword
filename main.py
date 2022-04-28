from tkinter import *
import random


GRID_SIZE = 10  # Ширина и высота игрового поля
SQUARE_SIZE = 40  # Размер одной клетки на поле
y = 1
x = 1

clicked = set()  # Создаем сет для клеточек, по которым мы кликнули

def click(event):
    ids = c.find_withtag(CURRENT)[0]  # Определяем по какой клетке кликнули
    c.itemconfig(CURRENT, fill="green")  # Иначе красим в зеленый
    c.update()

def clear(event):
    ids = c.find_withtag(CURRENT)[0]  # Определяем по какой клетке кликнули
    c.itemconfig(CURRENT, fill="gray")  # Иначе красим в зеленый
    c.update()

root = Tk()
root.title("JunCrossWorld")
c = Canvas(root, width=(GRID_SIZE * SQUARE_SIZE) + SQUARE_SIZE, height=(GRID_SIZE * SQUARE_SIZE) + SQUARE_SIZE)
c.bind("<Button-1>", click)
c.bind("<Button-3>", clear)
c.pack()

for i in range(GRID_SIZE+1):
    for j in range(GRID_SIZE+1):
        if i==0:
            label = Label(text='t', relief=FLAT, bd=1)
            label.pack()
            label.place(x=(SQUARE_SIZE*y)+18, y=10)
            y=y+1
        elif j==0:
            label = Label(text='t', bd=3)
            label.pack()
            label.place(x=14, y=(SQUARE_SIZE*x)+7)
            x = x + 1
        else:
            c.create_rectangle(i * SQUARE_SIZE, j * SQUARE_SIZE, i * SQUARE_SIZE + SQUARE_SIZE, j * SQUARE_SIZE + SQUARE_SIZE, fill='gray')

root.mainloop()