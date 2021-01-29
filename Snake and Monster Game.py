import turtle
import random
import time

food = {
    1: [0, 0], 2: [0, 0], 3: [0, 0], 
    4: [0, 0], 5: [0, 0], 6: [0, 0], 
    7: [0, 0], 8: [0, 0], 9: [0, 0]
    }
foodCompleted = {
    1: [300, 300], 2: [300, 300], 3: [300, 300], 
    4: [300, 300], 5: [300, 300], 6: [300, 300], 
    7: [300, 300], 8: [300, 300], 9: [300, 300]
    }
snakeDirection = ["", "unpause"]
directions = {'r': 0, 'u': 90, 'l': 180, 'd':270}
stampsLocation = []
tailsLength = 0
count = []

def setTurtle(pen, x, y):       # for setting a turtle position
    pen.speed(0)
    pen.penup()
    pen.setposition(x, y)

def writeFood():
    pen.clear()
    for i in food:
        setTurtle(foodPen, food[i][0], food[i][1])
        foodPen.write(i)

def rewriteFood():
    global tailsLength
    for i in food:                      # Checking for every food availability
        xDistance = abs(snake.xcor() - food[i][0])
        yDistance = abs(snake.ycor() - food[i][1])
        if xDistance < 20 and yDistance < 20:
            food[i] = [300, 300]        # Set food outside the frame
            tailsLength += i            # Save the food's value eaten
            foodPen.clear()
            writeFood()
    wn.ontimer(rewriteFood, 100)

def goRight():
    if snakeDirection[0] != "l":
        snakeDirection[0] = "r"
        snakeDirection[1] = "unpause"

def goUp():
    if snakeDirection[0] != "d":
        snakeDirection[0] = "u"
        snakeDirection[1] = "unpause"

def goLeft():
    if snakeDirection[0] != "r":
        snakeDirection[0] = "l"
        snakeDirection[1] = "unpause"

def goDown():
    if snakeDirection[0] != "u":
        snakeDirection[0] = "d"
        snakeDirection[1] = "unpause"

def move():
    global tailsLength
    delay = 200
    if (snake.distance(monster) >= 20 and food != foodCompleted
       and snakeDirection[0] != "" and snakeDirection[1] == "unpause"):
        snake.setheading(directions[snakeDirection[0]])
        snake.forward(20)
        # Making snake's tails
        snake.fillcolor("yellow")
        lack = tailsLength - len(stampsLocation) + 1
        if tailsLength > 0 and lack > 0:
            delay = 300
            snake.stamp()
            lack -= 1
            stampsLocation.append(snake.position())
        elif lack == 0:
            snake.stamp()
            stampsLocation.append(snake.position())
            snake.clearstamps(1)
            del(stampsLocation[0])
        snake.color("green")
        wn.update()
    wn.ontimer(move, delay)

def chase():
    if (snake.distance(monster) >= 20 and food != foodCompleted
       and snakeDirection[0] != ""):
        for aStampLocation in stampsLocation:       # Count body contact
            xDist = abs(monster.xcor() - aStampLocation[0])
            yDist = abs(monster.ycor() - aStampLocation[1])
            if xDist < 20 and yDist < 20:
                count.append('')
        xDistance = snake.xcor() - monster.xcor()
        yDistance = snake.ycor() - monster.ycor()
        if abs(xDistance) > abs(yDistance) and xDistance > 0:
            monster.goto(monster.xcor() + 20, monster.ycor())
        elif abs(xDistance) > abs(yDistance) and xDistance < 0:
            monster.goto(monster.xcor() - 20, monster.ycor())
        elif abs(yDistance) > abs(xDistance) and yDistance > 0:
            monster.goto(monster.xcor(), monster.ycor() + 20)
        elif abs(yDistance) > abs(xDistance) and yDistance < 0:
            monster.goto(monster.xcor(), monster.ycor() - 20)
    wn.ontimer(chase, random.randint(240, 300))

def pause():
    if snakeDirection[1] == "unpause":
        snakeDirection[1] = "pause"
    else:
        snakeDirection[1] = "unpause"

def main(x, y):
    startTime = time.time()
    writeFood()
    while True:
        wn.update()
        # Update title with game status
        title = "Body Contact: " + str(len(count)) + "    " + "Time: " + str(int(time.time() - startTime))
        wn.title(title)
        # Check and pause movement when colliding with the wall
        if abs(snake.xcor()) > 240 or abs(snake.ycor()) > 240:
            wn.tracer(0)
            snake.backward(20)
        elif food == foodCompleted:
            snake.write("Winner!", font = ("Arial", 12, "normal"))
            break
        elif snake.distance(monster) < 20:
            snake.write("Game Over!", font = ("Arial", 12, "normal"))
            break

# Set up game area
wn = turtle.Screen()
wn.title("Snake Game by Yelike")
wn.setup(width=500, height=500)

# Print game information
pen = turtle.Turtle()
pen.hideturtle()
setTurtle(pen, -210, 120)
pen.write("Welcome to Yelike's Snake-Monster Game!\n\n\n\n", font=("Arial", 12, "bold"))
pen.write("Use the 4 arrow keys to move the snake, and try to consume \n"
          "all the food items before the monster catches you\n", font=("Arial", 12, "normal"))
pen.write("Click anywhere on the screen to start the game!", font=("Arial", 10, "italic"))

# Making snake's head
snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
setTurtle(snake, 0, 0)

# Making monster
monster = turtle.Turtle()
monster.shape("square")
monster.color("red")
x, y = random.randint(-230, 230), random.randint(-230, 230)
while abs(x) < 60 or abs(y) < 60:       # Keep monster start further away from snake
    x, y = random.randint(-230, 230), random.randint(-230, 230)
setTurtle(monster, x, y)

# Assign food location (food = {1: [x, y], 2: . . . })
foodPen = turtle.Turtle()
foodPen.hideturtle()
for i in food:
    x, y = random.randint(-235, 235), random.randint(-235, 235)
    while abs(x) < 40 or abs(y) < 40:       # Avoid giving food too close to the snake
        x, y = random.randint(-235, 235), random.randint(-235, 235)
    food[i] = [x, y]

# Controls
wn.tracer(0)
wn.onclick(main)
wn.listen()
wn.onkey(goRight, "Right")
wn.onkey(goUp, "Up")
wn.onkey(goLeft, "Left")
wn.onkey(goDown, "Down")
wn.onkeypress(pause, "space")

# Motions
move()
rewriteFood()
chase()

wn.mainloop()