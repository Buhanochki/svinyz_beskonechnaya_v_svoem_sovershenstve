import time
from tkinter import *
import random

class Balls():
    def __init__(self, canvas, coords = [50, 50, 100, 100]):
        self.canvas = canvas
        self.oval = self.canvas.create_oval(coords[0],coords[1],coords[2],coords[3], fill = 'white')
        self.speed_y = random.randint(1,4)
        self.speed_x = random.randint(1,4)
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
        
def click(event):
    for ball in range(len(ball_list)):
        crd = ball_list[ball].get_coords()
        if event.x in range(ball_list[ball].get_coords()[0], ball_list[ball].get_coords()[2]) and event.y in range(ball_list[ball].get_coords()[1], ball_list[ball].get_coords()[3]):
            ball_list[ball].change_color()
            del ball_list[ball]
            ball_list.append(Balls(canvas, crd))
            ball_list.append(Balls(canvas, crd))
            


WIDTH = 600
HEIGHT = 600
PAD = 20
tk = Tk()
tk.geometry(f'{WIDTH}x{HEIGHT}')

canvas = Canvas(width = WIDTH - PAD * 2, height = HEIGHT - PAD * 2, bg = 'black')
canvas.place(x = PAD, y = PAD)

ball_list = []
ball_list.append(Balls(canvas))
ball_list.append(Balls(canvas))
ball_list.append(Balls(canvas))
ball_list.append(Balls(canvas))
ball_list.append(Balls(canvas))
ball_list.append(Balls(canvas))

canvas.bind_all('<Button-1>', click)

while 1:
    for ball in ball_list:                  
        ball.move()
        
    time.sleep(0.01)
    tk.update()