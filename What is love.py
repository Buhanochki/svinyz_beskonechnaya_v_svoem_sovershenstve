import time
from tkinter import *
import random

class Balls():
    def __init__(self, canvas, coords = [50, 50, 100, 100], speed_x = 1, speed_y = 1, decr = 0):
        self.decr = decr
        self.canvas = canvas    
        if decr != 0:
            self.oval = self.canvas.create_oval(coords[0] + decr,coords[1] + decr,coords[2] - decr,coords[3] - decr, fill = 'white')
        else:
            self.oval = self.canvas.create_oval(coords[0],coords[1],coords[2],coords[3], fill = 'white') 
        self.speed_y = speed_y
        self.speed_x = speed_x
    def move(self):
        self.crd = self.canvas.coords(self.oval)
        if self.crd[0] <= 0:
            self.speed_x *= -1
        if self.crd[1] <= 0:
            self.speed_y *= -1
        if self.crd[2] >= 560:
            self.speed_x *= -1
        if self.crd[3] >= 560:
            self.speed_y *= -1
        self.canvas.move(self.oval, self.speed_x, self.speed_y)
    def change_color(self):
        self.canvas.delete(self.oval)
    def get_coords(self):
        return list(map(int, self.canvas.coords(self.oval)))
cnt = 0        
def click(event):
    for ball in range(len(ball_list)):
        if event.x in range(ball_list[ball].get_coords()[0], ball_list[ball].get_coords()[2]) and event.y in range(ball_list[ball].get_coords()[1], ball_list[ball].get_coords()[3]):
            ball_list[ball].change_color()
            crd = ball_list[ball].get_coords()
            ball_list.append(Balls(canvas, crd, -1, 1, decr=10))
            ball_list.append(Balls(canvas, crd, 1, -1, decr=10))
            ball_list.append(Balls(canvas, crd, -1, -1, decr=10))
            ball_list.append(Balls(canvas, crd, 0, 1, decr=10))
            ball_list.append(Balls(canvas, crd, -1, 0, decr=10))
            ball_list.append(Balls(canvas, crd, 0, -1, decr=10))
            ball_list.append(Balls(canvas, crd, 0, -1, decr=10))
            ball_list.append(Balls(canvas, crd, 1, 0, decr=10))
            ball_list.append(Balls(canvas, crd, decr=10))
            del ball_list[ball]

            


WIDTH = 600
HEIGHT = 600
PAD = 20
tk = Tk()
tk.geometry(f'{WIDTH}x{HEIGHT}')
label = Label(text='0')
label.pack
canvas = Canvas(width = WIDTH - PAD * 2, height = HEIGHT - PAD * 2, bg = 'black')
canvas.place(x = PAD, y = PAD)

ball_list = []
ball_list.append(Balls(canvas))

canvas.bind_all('<Button-1>', click)

while 1:
    for ball in ball_list:                  
        ball.move()
        label.config(text=str(cnt))
    time.sleep(0.01)
    tk.update()
    ((((((((((((((((((((()))))))))))))))))))))