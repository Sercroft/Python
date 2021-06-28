from random import *
from turtle import *
from freegames import vector

#Inicializando la posición del pájaro y el contador de bolas
bird = vector (0,0)
balls = []

#Movimiento
def tap(x,y):
    up = vector(0,50)
    bird.move(up)

def inside(point):
    return -200 < point.x <200 and -200 < point.y < 200

def draw(alive):
    clear()

    goto(bird.x,bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10,'red')
        print('Game Over')

    for ball in balls:
        goto(ball.x,ball.y)
        dot(20, 'black')

    update()

def move():
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange (10) == 0:
        y = randrange(-199,199)
        ball = vector (199,y)
        balls.append(ball)

    while len(balls) > 0 and not inside (balls[0]):
        balls.pop()

    if not inside (bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move,50)

    
setup(420,420,370,0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()



