import turtle
import time
turtle.bgpic("bg.gif")
lines = turtle.clone()
lines.penup()
lines.hideturtle()
##turtle.hideturtle()
lines.goto(0,300)
lines.pendown()
lines.color('white')
lines.write("Clairdan Saving The Environment!" , align = 'center', font= ('impact', 30, "normal"))
lines.penup()
lines.goto(0,350)
lines.pendown()
lines.goto(470,350)
lines.goto(470,-350)
lines.goto(-470,-350)
lines.goto(-470,350)
lines.goto(0,350)
lines.penup()
SIZE_X=700
SIZE_Y=400
turtle.setup(1000, 1000)
turtle.register_shape("clairdan.gif")
turtle.register_shape("clairdan_back.gif")
turtle.register_shape("enemy.gif")
clairdan = turtle.clone()
enemy = turtle.clone()
enemy.shape("enemy.gif")
clairdan.shape("clairdan.gif")

enemy.shape("enemy.gif")
clairdan.penup()
enemy.penup()

clairdan.goto(-200,40)
enemy.goto(200,-80)


