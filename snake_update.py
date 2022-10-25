from tkinter import *
import random
from tkinter import font
from turtle import speed
from turtle import window_height, window_width


window = Tk()
window.title("PYTHON SNAKE GAME")
window.resizable(0,0)

label = Label(window, font='arial 20 bold', text='CodewithCollins').pack(side=BOTTOM)#footer
score = 0
direction = 'down'
GAME_HEIGHT = 600
GAME_WIDTH = 600
SPEED = 50
SPACE_SIZE = 20
BODY_PARTS = 4
SNAKE_COLOUR = '#00FF00'
FOOD_COLOUR = '#FF0000'


Label = Label(window, bg= "white", text = 'score:{}'.format(score), font=('gameplay', 40))
Label.pack()


canvas = Canvas(window, bg="black", height= GAME_HEIGHT, width= GAME_WIDTH  )
canvas.pack()


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square = canvas.create_oval(x , y,  x + SPACE_SIZE, y +SPACE_SIZE, fill = SNAKE_COLOUR, tag = "snake")
            self.squares.append(square)
        


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE) - 1)* SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE) - 1)* SPACE_SIZE

        self.coordinates = [x,y]
        canvas.create_oval(x, y,  x + SPACE_SIZE, y +SPACE_SIZE, fill= FOOD_COLOUR, tag = 'food')

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2 , canvas.winfo_height()/2, font=("gameplay 60 bold"), text="GAME OVER", fill="red", tag="game over")


def next_turn(snake,food):
    x,y = snake.coordinates[0]
    if direction == 'up':
        y = y - SPACE_SIZE
    elif direction == 'down':
        y = y + SPACE_SIZE
    elif direction == 'left':
        x = x - SPACE_SIZE
    elif direction == 'right':
        x = x + SPACE_SIZE


    snake.coordinates.insert(0, (x,y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOUR )
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score

        score =  score + 1
        Label.config(text = 'score:{}'. format(score))
        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    if direction == "left":
        #if direction != "right":
        direction = new_direction
    elif direction == "right":
        #if direction != "left":
        direction = new_direction
    elif direction == "up":
        #if direction != "down":
        direction = new_direction
    elif direction == "down":
        #if direction != "up": 
        direction = new_direction

def check_collisions(snake):
    x,y = snake.coordinates[0]
    if x<0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_WIDTH:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    



window.update()

window_width = window.winfo_width()
window_height =window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event:change_direction('left'))
window.bind("<Right>", lambda event:change_direction('right'))
window.bind("<Up>", lambda event:change_direction('up'))
window.bind("<Down>", lambda event:change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()


