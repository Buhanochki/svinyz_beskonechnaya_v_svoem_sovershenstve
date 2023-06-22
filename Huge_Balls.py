from tkinter import *
import time

class Gui():
    def __init__(self, title, side_size, padding, background_color):
        self.title = title
        self.background_color = background_color
        self.side_size = side_size
        self.padding = padding

        self.tk = Tk()
        self.tk.geometry(f'{self.side_size + self.padding * 2}x{self.side_size + self.padding * 2}')
        self.tk.title(title)
        self.tk.resizable(False, False)
        
        self.canvas = Canvas(self.tk, width=self.side_size, height = self.side_size, bg=self.background_color )
        self.canvas.place(x = self.padding, y = self.padding)

        self.sprites: list[Ball] = []
        self.canvas.bind_all('<Button-1>', self.click)

    def create_ball(self, x, y):
        self.sprites.append(Ball(self,vel_x=x, vel_y=y, center_x=200, center_y=200, radius=20))



    def get_coords(self, ball_id):
        return list(map(int, self.canvas.coords(ball_id)))
    
    def click(self, event):
        for ball in range(len(self.sprites)):
            if event.x in range(self.get_coords(self.sprites[ball].oval)[0], self.get_coords(self.sprites[ball].oval)[2]) and event.y in range(self.get_coords(self.sprites[ball].oval)[1], self.get_coords(self.sprites[ball].oval)[3]):
                self.sprites[ball].delete_ball()
                crd = self.get_coords(self.sprites[ball].oval)
                self.sprites.append(self.sprites[ball].create_child(-1, 1))
                self.sprites.append(self.sprites[ball].create_child(1, -1))
                self.sprites.append(self.sprites[ball].create_child(-1, -1))
                self.sprites.append(self.sprites[ball].create_child(0, 1))
                self.sprites.append(self.sprites[ball].create_child(-1, 0))
                self.sprites.append(self.sprites[ball].create_child(0, -1))
                self.sprites.append(self.sprites[ball].create_child(1, 0))
                self.sprites.append(self.sprites[ball].create_child(1, 1))
                del self.sprites[ball]

    def mainloop(self):
        while True:
            self.sprites[0].move()
            time.sleep(0.01)
            self.tk.update()
            print(len(self.sprites))
class Ball():
    def __init__(self, gui: Gui , vel_x, vel_y, center_x, center_y, radius):


        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.gui = gui
        self.oval = self.gui.canvas.create_oval(self.center_x - self.radius,
                                                 self.center_y - self.radius,
                                                   self.radius + self.center_x,
                                                    self.radius + self.center_y, 
                                                      fill = 'white')
        self.vel_x = vel_x
        self.vel_y = vel_y
    '''def __proletariat(self):
        work.do()'''
    def move(self):
        self.crd = self.gui.canvas.coords(self.oval)
        if self.crd[0] <= 0:
            self.vel_x *= -1
        if self.crd[1] <= 0:
            self.vel_y *= -1
        if self.crd[2] >= 500   :
            self.vel_x *= -1
        if self.crd[3] >= 500:
            self.vel_y *= -1
        self.gui.canvas.move(self.oval, self.vel_x, self.vel_y)
        self.center_update()

    def center_update(self):
        self.center_y += self.vel_y
        self.center_x += self.vel_x

    def delete_ball(self):
        self.gui.canvas.delete(self.oval)
        
    def create_child(self, vel_x, vel_y):
        self.gui.sprites.append(Ball(vel_x=vel_x, vel_y=vel_y, radius=self.radius / 2, center_x=self.center_x, center_y=self.center_y)) 
           
g = Gui('geometry', 500, 20, 'black')
g.create_ball(1, 1)
g.mainloop()
