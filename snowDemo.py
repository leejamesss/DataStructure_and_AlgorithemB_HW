# import turtle 
# def snow(n,size):
#     if n==0:
#         turtle.forward(size)
#         return
#     snow(n-1,size/3)
#     turtle.left(60)
#     snow(n-1,size/3)
#     turtle.right(120)
#     snow(n-1,size/3)
#     turtle.left(60)
#     snow(n-1,size/3)
# def main():
#     turtle.setup(600,600)
#     turtle.penup()
#     turtle.goto(-200,100)
#     turtle.pendown()
#     turtle.pensize(2)
#     level=3
#     size=400
#     snow(level,size)
#     turtle.hideturtle()

# main()



# import turtle
# def snow(n,size):
#     if n==1:
#         turtle.fd(size)
#     else:
#         for angle in [0,60,-120,60]:
#             turtle.lt(angle)
#             snow(n-1,size/3)

# turtle.setup(800,800)
# turtle.speed(10000000)
# turtle.penup()
# turtle.goto(-300,-100)
# turtle.pendown()
# snow(4,600)



import turtle
def snow(n,size):
    if n==1:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.lt(angle)
            snow(n-1,size/3)

# turtle.setup(800,800)
# turtle.speed(10000000)
# turtle.penup()
# turtle.goto(-300,-100)
# turtle.pendown()
# snow(4,600)
# turtle.done()


turtle.setup(800,800)
turtle.speed(1000)
turtle.penup()
turtle.goto(-300,100)
turtle.pendown()
turtle.pensize(2)
level =3
snow(level, 400)
turtle.right(120) #右拐 120 度
snow(level, 400)
turtle.right(120)
snow(level, 400)
turtle.done()


