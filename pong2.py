import turtle
import random

#tela
screen = turtle.Screen()
screen.title("PONG")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

#pontos
pontosJ1 = 0
pontosJ2 = 0

#pontos na tela
pontos = turtle.Turtle()
pontos.speed(0)
pontos.color("white")
pontos.penup()
pontos.hideturtle()
pontos.goto(0,260)
pontos.write("Player A: 0  Player B: 0",align="center",font=("Arial",20,"normal"))


#jogadores
#jogador 1
j1 =turtle.Turtle()
j1.speed(0)
j1.shape("square")
j1.color("white")
j1.penup()
j1.shapesize(stretch_wid=5,stretch_len=1)
j1.goto(-350,0)

#jogador 2
j2 =turtle.Turtle()
j2.speed(0)
j2.shape("square")
j2.color("white")
j2.penup()
j2.shapesize(stretch_wid=5,stretch_len=1)
j2.goto(350,0)

#bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0,0)
bola.dx = -0.2 
bola.dy = 0.2



#Funtions
def moveUp_1():
    y = j1.ycor()
    y +=10.0
    j1.sety(y)

def moveUp_2():
    y = j2.ycor()
    y += 10.0
    j2.sety(y)

def moveDown_1():
    y = j1.ycor()
    y -=10.0
    j1.sety(y)

def moveDown_2():
    y = j2.ycor()
    y -= 10.0
    j2.sety(y)


screen.listen()
screen.onkeypress(moveUp_1,"w")
screen.onkeypress(moveDown_1,"s")

screen.onkeypress(moveUp_2,"Up")
screen.onkeypress(moveDown_2,"Down")

while True:
    screen.update()
    #movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    if bola.ycor() > 290:#confere se colidiu com a parte de cima
        bola.sety(290)   #define a altura da bola
        bola.dy*=-1      #inverte a direção no eixo y
    elif bola.ycor() < -290:#confere se colidiu com a parte de baixo
        bola.sety(-290)     #define a altura da bola
        bola.dy*=-1         #inverte a direção no eixo y
    #resetar a bola quando sair da tela
    if bola.xcor() > 410:
        pontosJ1+=1
        pontos.clear()
        #pontuação
        pontos.write("Player A: {}  Player B: {}".format(pontosJ1,pontosJ2),align="center",font=("Arial",20,"normal"))
        bola.goto(0,0)
        bola.dx*=-1.0
    elif bola.xcor() < -410:
        pontosJ2+=1
        pontos.clear()
        #pontuação
        pontos.write("Player A: {}  Player B: {}".format(pontosJ1,pontosJ2),align="center",font=("Arial",20,"normal"))
        bola.goto(0,0)
        bola.dx*=-1
        
    #colisão com os jogadores     
    if (bola.xcor()>340 and bola.xcor() < 350) and (bola.ycor() < j2.ycor()+50 and bola.ycor() > j2.ycor()-50):
        bola.setx(340)
        bola.dx*=-1
    elif (bola.xcor()<-340 and bola.xcor() > -350) and (bola.ycor() < j1.ycor()+50 and bola.ycor() >  j1.ycor()-50):
        bola.setx(-340)
        bola.dx*=-1
    #limites dos jogaores
    if j1.ycor() > 250:
        j1.sety(250)
    elif j1.ycor()<-250:
        j1.sety(-250)
    
    if j2.ycor() > 250:
        j2.sety(250)
    elif j2.ycor()<-250:
        j2.sety(-250)
