import random
from turtle import Turtle, Screen


def rgb_to_color(tup):
    r = tup[0]
    g = tup[1]
    b = tup[2]
    return "#%02x%02x%02x" % (r, g, b)

# Code to extract colors from a painting:
# import colorgram
# colors = colorgram.extract("image.jpg", 50)
# range_of_colors = []
# for i in range(len(colors)):
#     color = colors[i]
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     col_tup = (r, g, b)
#     range_of_colors.append(col_tup)
# print(range_of_colors)


tim = Turtle()
y = -250
color_list = [(245, 242, 236), (245, 236, 241), (227, 233, 241), (235, 243, 239), (212, 158, 87), (237, 214, 96), (36, 105, 148), (150, 77, 54), (126, 168, 197), (206, 135, 162), (153, 62, 81), (24, 40, 56), (209, 86, 63), (172, 160, 51), (197, 88, 120), (136, 183, 152), (55, 119, 92), (25, 42, 35), (226, 169, 186), (64, 46, 35), (238, 213, 6), (89, 156, 102), (38, 164, 186), (10, 97, 74), (41, 59, 100), (178, 190, 214), (96, 126, 173), (229, 174, 166), (67, 35, 44), (104, 43, 61), (171, 204, 182), (111, 44, 38), (76, 69, 38), (156, 206, 216), (6, 89, 113)]

tim.penup()
tim.goto(-250, y)
tim.pendown()
for j in range(10):
    for i in range(10):
        tim.dot(20, rgb_to_color(random.choice(color_list)))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    y += 50
    tim.penup()
    tim.goto(-250, y)
    tim.pendown()

screen = Screen()
screen.exitonclick()