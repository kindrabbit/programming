import turtle

turtle.screensize(800, 600, "green")

turtle.setheading(-45)

turtle.circle(90, 360, 40)
turtle.circle(-90, 360, 40)
turtle.setheading(-135)
turtle.circle(90, 360, 40)
turtle.circle(-90, 360, 40)
turtle.setheading(45)

turtle.goto(0,-300)
# turtle.circle(90, 90, 10)
# turtle.circle(-90, 360, 40)
# turtle.circle(90, 90, 10)
# turtle.circle(-90, 360, 40)
# turtle.circle(90, 90, 10)
# turtle.circle(-90, 360, 40)
# turtle.circle(90, 90, 10)
# turtle.circle(-90, 360, 40)
# turtle.circle(90, 360, 40)
#
# #turtle.circle(90, 90, 10)
# turtle.circle(-90, 360, 40)

#
# # 2
# a = 1
# b = 1
# for a in range(0, 10, 1):
#     a = a + 1
#     turtle.pensize(b)
#     turtle.circle(a * 10)
#     turtle.circle(-a * 10)
#
# # 3
# a = 1
# b = 1
# while a < 20:
#     a = a + 1
#     b = b + 1
#     if a % 2 == 0:
#         continue
#     turtle.pensize(b + 2)
#     turtle.circle(a * 10)
#     turtle.circle(-a * 10)
#     if a == 6:
#         turtle.done()
#         break

# turtle.done()
turtle.exitonclick()
