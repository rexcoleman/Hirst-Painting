import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(233, 225, 97), (209, 164, 95), (112, 176, 210), (216, 65, 125), (185, 75, 39), (205, 140, 175), (178, 48, 105), (117, 189, 146), (52, 92, 157), (17, 22, 61), (23, 28, 162), (220, 72, 48), (221, 173, 198), (178, 153, 53), (63, 113, 74), (20, 44, 29), (65, 27, 14), (86, 167, 95), (99, 97, 202), (138, 29, 63), (59, 16, 28), (133, 214, 232), (154, 211, 193), (170, 184, 229), (138, 33, 23), (36, 83, 51)]

number_of_dots = 100

tim.speed(0)
tim.up()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    print(dot_count)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()