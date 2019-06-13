import turtle 
def draw_square(length,color):
        turtle.color(color)
        for x in range (4):
            turtle.forward(length)
            turtle.right(90)
    
draw_square(200,"red")
turtle. mainloop()

