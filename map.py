import turtle


def initialize_resolution():
    """This function is used for configure resolution settings"""
    turtle.screensize()
    turtle.setup(width = 1.0, height = 1.0)
    turtle.speed(0)
    turtle.Screen().setup(1200, 630)
    turtle.title("TURTLE RACE")
    turtle.Screen().bgpic('resources/race_background.png')


def draw_finish_line(posX, posY):
    """Draw a finish line at the end of the map"""
    turtle.penup()
    turtle.setpos(posX, posY)
    turtle.left(90)
    turtle.pensize(5)
    turtle.pendown()
    turtle.forward(520)
    turtle.penup()
    turtle.forward(200)


def draw_map(level):
    """Draw the whole map"""
    initialize_resolution()
    setY_map_line = 300

    turtle.penup()
    turtle.setpos(-100 * level - 200, setY_map_line)
    if level == 1:
        length_of_map = 20
        setX_map_line = 80
    elif level == 2:
        length_of_map = 40
        setX_map_line = 380
    else:
        length_of_map = 50
        setX_map_line = 480

    for draw_number in range(int(length_of_map / 2)):
        turtle.write(draw_number, align='center', font=("Roboto", 10))
        turtle.forward(40)

    turtle.pensize(3)
    turtle.right(180)
    setY_map_line -= 20
    
    for i in range(5):
        turtle.penup()
        turtle.setpos(setX_map_line, setY_map_line)
        turtle.pendown()
        turtle.forward(length_of_map * 20)
        setY_map_line -= 130

    draw_finish_line(setX_map_line, 280)
