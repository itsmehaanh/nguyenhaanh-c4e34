import turtle 
def draw_square(length,color):
        window = turtle.Screen()
        t = turtle.Turtle()
        t.pencolor(color)
        for x in range (4):
            t.forward(length)
            t.right(90)
    
draw_square(200,"red")

