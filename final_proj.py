import turtle
import time
turtle.tracer(1,0)
turtle.register_shape('bg.gif')
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
run = turtle.clone()
ability = turtle.clone()
lattack = turtle.clone()
pattack = turtle.clone()
turtle.register_shape("pattack.gif")
turtle.register_shape("lattack.gif")
turtle.register_shape("ability.gif")
turtle.register_shape("run.gif")
enemy.shape("enemy.gif")
clairdan.shape("clairdan.gif")
run.shape("run.gif")
ability.shape("ability.gif")
lattack.shape("lattack.gif")
pattack.shape("pattack.gif")
run.penup()
pattack.penup()
lattack.penup()
ability.penup()
clairdan.penup()
enemy.penup()

clairdan.goto(-200,40)
enemy.goto(200,-80)
pattack.goto(-365,-250)
ability.goto(120,-250)
lattack.goto(-120,-250)
run.goto(365,-250)

#def lesser_attack():
    




    







