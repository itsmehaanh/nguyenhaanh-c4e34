import turtle 
def draw_square(length,color):
        turtle.color(color)
        for x in range (4):
            turtle.forward(length)
            turtle.right(90)
    
draw_square(200,"red")

for i in range(30):
    draw_square(i * 5, 'red')
    turtle.left(17)
    turtle.penup()
    turtle.forward(i * 2)
    turtle.pendown()

turtle. mainloop()