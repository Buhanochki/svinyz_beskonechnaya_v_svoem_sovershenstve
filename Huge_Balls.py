from tkinter import *
import time

class Gui():
    colesa = [(-1, 1),(1, -1),(0, 1),(-1, 0),(0, -1),(1, 0),(-1, -1),(1, 1)]
    def __init__(self, title, side_size, padding, background_color):
        self.title = title
        self.background_color = background_color
        self.side_size = side_size
        self.padding = padding

        self.tk = Tk()
        self.tk.geometry(f'{self.side_size + self.padding * 2}x{self.side_size + self.padding * 2 + 30 + 50}')
        self.tk.title(title)
        self.tk.resizable(False, False)
        
        self.canvas = Canvas(self.tk, width=self.side_size, height = self.side_size, bg=self.background_color )
        self.canvas.place(x = self.padding, y = self.padding)

        self.score_counter = Label(self.tk, text='0', font=('Arial',25))
        self.counter = 0
        self.score_counter.place(x=(self.side_size + self.padding * 2) / 2, y = self.side_size + self.padding + 5)

        self.time_counter = Label(self.tk, text='0', font=('Arial', 25))
        self.time_start = time.time()
        self.time_counter.place(x=(self.side_size + self.padding * 2) / 2, y = self.side_size + self.padding + 5 + 50)

        self.sprites: list[Ball] = []
        self.canvas.bind_all('<Button-1>', self.click)

        self.restart_button = Button(self.tk, text = 'reset', font=('Arial', 25))
        self.restart_button.config(command=self.restart)
        self.restart_button.place(x=padding, y = self.side_size + self.padding + 5)

    def create_ball(self, x, y):
        self.sprites.append(Ball(self,vel_x=x, vel_y=y, center_x=200, center_y=200, radius=20))
    def restart(self):
        for ball in self.sprites:
            ball.delete_ball()
        self.sprites = []
        self.score_counter.config(text='0')
        self.counter = 0
        self.time_counter.config(text='0.00')
        self.time_start = time.time()
        self.create_ball(1,1)
    def clear_field(self):
        for ball in self.sprites:
            ball.delete_ball()
        self.sprites = []

    def get_coords(self, ball_id):
        return list(map(int, self.canvas.coords(ball_id)))
    
    def click(self, event):
        for ball in self.sprites:
                coords = self.get_coords(ball.oval)
                if event.x in range(coords[0],coords[2]) and event.y in range(coords[1], coords[3]):
                    self.counter += 1
                    if ball.radius > 5:
                        ball.delete_ball()
                        for e in range(8):
                            ball.create_child(self.colesa[e][0], self.colesa[e][1])
                        del self.sprites[self.sprites.index(ball)]
                        break
                    else:
                        ball.delete_ball()
                        del self.sprites[self.sprites.index(ball)]
                

    def mainloop(self):
        while True:
            for ball in self.sprites:
                ball.move()
                self.score_counter.config(text=str(self.counter))
                self.time_counter.config(text=str(round(time.time() - self.time_start, 2)))
                print(round(time.time() - self.time_start, 2) > 30.00)
                if round(time.time() - self.time_start, 2) > 30.00:
                    self.clear_field
            time.sleep(0.01)
            self.tk.update()
            #print(len(self.sprites))
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
        #print(self.crd)
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
        self.gui.sprites.append(Ball(gui=self.gui, vel_x=vel_x, vel_y=vel_y, radius=self.radius - 5, center_x=self.center_x, center_y=self.center_y)) 
           
g = Gui('geometry', 500, 20, 'black')
g.create_ball(1, 1)
g.mainloop()
