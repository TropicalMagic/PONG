from tkinter import *
import random
import time

counter=0
counter2=0

tk = Tk()
tk.title("PONG!")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=800,height=800,bd=0,highlightthickness=0)
canvas.config(bg="black")
##black background for pong
canvas.pack()
tk.update()

canvas.create_line(400,0,400,800,fill="white")

class Ball:
    def __init__(self,canvas,color,paddle,paddle2):
        self.canvas=canvas
        self.paddle=paddle
        self.paddle2=paddle2
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,235,200)
        starts=[-3,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=800


    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False
        
    def hit_paddle2(self,pos):
        paddle_pos=self.canvas.coords(self.paddle2.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
            return False

    def draw(self):
        
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>= self.canvas_height:
            self.y=-3
        if pos[0] <= 0:
            self.x=3
            self.score=True
        if pos[2] >= self.canvas_width:
            self.x=-3
            self.score=False
        if self.hit_paddle(pos) == True:
            self.x=3
        if self.hit_paddle2(pos) == True:
            self.x=-3

    def score(self,val):
        global counter
        global counter2

        if val == True:
            a = self.canvas.create_text(400,40,text=counter,font=("Times New Roman",60),fill="white")
            canvas.itemconfig(a,fill="black")
            counter+=1
            a = self.canvas.create_text(400,40,text=counter,font=("Times New Roman",60),fill="white")

        if val == False:
            a = self.canvas.create_text(775,40,text=counter2,font=("Times New Roman",60),fill="white")
            canvas.itemconfig(a,fill="black")
            counter2+=1
            a = self.canvas.create_text(775,40,text=counter2,font=("Times New Roman",60),fill="white")
        

class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,150,30,250,fill=color)
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('w',self.turn_left)
        self.canvas.bind_all('s',self.turn_right)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y=0
        if pos[3] >= 400:
            self.y=0

    def turn_left(self,evt):
        self.y=-3
    def turn_right(self,evt):
        self.y=3

class Paddle2:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(770,150,800,250,fill=color)
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.y=0
        self.canvas.bind_all('<KeyPress-Down>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Up>',self.turn_right)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y=0
        if pos[3] >= 800:
            self.y=0

    def turn_left(self,evt):
        self.y=3
    def turn_right(self,evt):
        self.y=-3
        
paddle=Paddle(canvas,"blue")
paddle2=Paddle2(canvas,"blue")
ball=Ball(canvas,"orange",paddle,paddle2)


while 1:
    ball.draw()
    paddle.draw()
    paddle2.draw()  
    if counter == 10:
        ball.x=0
        ball.y=0
        paddle.y=0
        paddle2.y=0
        canvas.create_text(450,400,text="Congrats Player 1! You Win!", font=32, fill="red")
        canvas.create_text(450,415,text="Score:" +str(counter)+ "-" + str(counter2), font=32, fill="red")
    if counter2 == 10:
        ball.x=0
        ball.y=0
        paddle.y=0
        paddle2.y=0
        canvas.create_text(450,400,text="Congrats Player 2! You Win!", font=32, fill="red")
        canvas.create_text(450,415,text="Score:" +str(counter)+ "-" + str(counter2), font=32, fill="red")

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

    if counter == 10 or counter2 == 10:
        time.sleep(10000)
