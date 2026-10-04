from turtle import *


# we want to print a house using turtle graphics

#step 1: draw a square 
speed(30)
width(7)
color("blue")

forward(200)
left(90)

forward(200) 
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door   
forward(70)
begin_fill()
color("red")
left(90)
forward(120) #heigt of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)          #drawing the roof
left(120)
forward(200)
end_fill()


penup()
goto(25, 120)
pendown()


color("brown", "yellow")
begin_fill()
left(30)
forward(30)  #drawing the window
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

penup()
goto(150, 120)      
pendown()


color("brown", "yellow")
begin_fill()
left(90)
forward(30)  #drawing the window
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()



exitonclick()