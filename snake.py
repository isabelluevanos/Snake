"""Snake, classic arcade game.

Programadores
1. Isabel Cristina Valdes Luevanos 
2. Víctor Hugo Portilla Ortíz

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

"""Initial values"""
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

"""Hexadecimal colors for snake and food"""
colorsSnake = ["#7e0374","#f55f93","#eda240", "#88beff","#99ffee"]
colorsFood = ["#0d710d", "#0d1571", "#9e104b", "#803706", "#156b6b"]

"""Random colors for snake and food"""
chooseCSnake = colorsSnake [randrange(0,5)]
chooseCFood = colorsFood [randrange(0,5)]

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)


    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, chooseCSnake)

    square(food.x, food.y, 9, chooseCFood)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
