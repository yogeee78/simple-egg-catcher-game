import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Egg Catcher Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Create the basket
basket = turtle.Turtle()
basket.shape("square")
basket.color("green")
basket.shapesize(stretch_wid=1, stretch_len=5)
basket.penup()
basket.goto(0, -250)

# Create a list to store eggs
eggs = []

def create_egg():
    egg = turtle.Turtle()
    egg.shape("circle")
    egg.color("yellow")
    egg.shapesize(stretch_wid=1, stretch_len=2)
    egg.penup()
    egg.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(150, 270)
    egg.goto(x, y)
    eggs.append(egg)

def move_basket_left():
    x = basket.xcor()
    x -= 20
    if x < -290:
        x = -290
    basket.setx(x)

def move_basket_right():
    x = basket.xcor()
    x += 20
    if x > 290:
        x = 290
    basket.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_basket_left, "Left")
screen.onkeypress(move_basket_right, "Right")

# Main game loop
while True:
    create_egg()

    for egg in eggs:
        y = egg.ycor()
        y -= 20
        egg.sety(y)

        # Check if the egg is caught
        if (basket.xcor() - 40 < egg.xcor() < basket.xcor() + 40) and (basket.ycor() - 20 < egg.ycor() < basket.ycor() + 20):
            egg.hideturtle()
            eggs.remove(egg)

    # Remove eggs that go out of the screen
    eggs = [egg for egg in eggs if egg.ycor() > -300]

    screen.update()
