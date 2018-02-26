from animal import Animal
from random import randint
from get_user_info import bet, get_name
from turtle import Turtle
from map import draw_map
import time
from decimal import Decimal
import turtle
from score_board import endgame_board


def set_up_start_position(level):
    start_position = [0 for i in range(5)]
    start_position[0] = 215
    start_position[1] = 85
    start_position[2] = -45
    start_position[3] = -175
    if level == 1: start_position[4] = -300
    elif level == 2: start_position[4] = -400
    else: start_position[4] = -500
    return start_position


def random_color():
    color = [0 for i in range(4)]
    get_random = [0 for i in range(4)]
    for i in range(4):
        while True:
            get_random[i] = randint(0, 3)
            available = True
            for j in range(i):
                if get_random[i] == get_random[j]:
                    available = False
                    break
            if available: break
    for i in range(4):
        if get_random[i] == 0:
            color[i] = 'yellow'
        elif get_random[i] == 1:
            color[i] = 'red'
        elif get_random[i] == 2:
            color[i] = 'green'
        else: color[i] = 'blue'
    return color


def set_up_turtle(level):
    name = [0 for i in range(4)]
    animals = [0 for i in range(4)]
    start_position = set_up_start_position(level)
    name[0], name[1], name[2], name[3] = get_name()
    choose = bet()
    color = random_color()
    animals[0] = Animal(name[0], color[0], start_position[4], start_position[0], 0, 2, 'turtle')
    animals[1] = Animal(name[1], color[1], start_position[4], start_position[1], 0, 2, 'turtle')
    animals[2] = Animal(name[2], color[2], start_position[4], start_position[2], 0, 2, 'turtle')
    animals[3] = Animal(name[3], color[3], start_position[4], start_position[3], 0, 2, 'turtle')
    return name, choose, animals


def set_up_rule(animals, check_available, length_of_map):
    while True:
        turn = randint(0, 3)
        if not check_available[0][turn] and animals[turn].step < length_of_map:
            check_available[0][turn] = True
            break

    # Random nước đi thẳng hoặc nước đi lùi. Nếu lượt trước đã đi lùi thì lượt này sẽ được đi thẳng
    un_lucky_move = randint(0, 10)
    check_available[2][turn] += 1
    if un_lucky_move < 3 and check_available[2][turn] > 1:  # Cứ mỗi 5 lượt đi thì chỉ được lùi 1 lần
        un_lucky_move += 10
    elif check_available[2][turn] == 5:
        check_available[2][turn] = 0
    if check_available[1][turn] or un_lucky_move < 3:
        rotate = 180
        check_available[1][turn] = not check_available[1][turn]
    else:
        rotate = 0
    return turn, un_lucky_move, check_available, rotate


def mark_rank(animal, rank, elapsed_time):
    if rank == 1:
        text = '1st: ' + str(elapsed_time) + 's'
    elif rank == 2:
        text = '2nd: ' + str(elapsed_time) + 's'
    elif rank == 3:
        text = '3rd: ' + str(elapsed_time) + 's'
    else:
        text = '4th: ' + str(elapsed_time) + 's'
    mark = Turtle()
    mark.color(animal.color)
    mark.hideturtle()
    mark.penup()
    mark.goto(animal.startX + animal.step - 350, animal.startY - 30)
    mark.pendown()
    mark.write(text, font=("Roboto", 40))


def race(animals, check_available, length_of_map):
    check_if_win = False
    rank = 1
    score = [0 for i in range(4)]
    start_time = time.time()
    while animals[0].step + animals[1].step + animals[2].step + animals[3].step < length_of_map * 4:
        turn, un_lucky_move, check_available, rotate = set_up_rule(animals, check_available, length_of_map)

        #Di chuyển
        if animals[turn].step < length_of_map:
            step = randint(0, length_of_map / 2)
            if check_available[1][turn]: #Giới hạn độ dài lùi tối đa là 50 bước
                step = 50
            elif (not check_available[1][turn] or rotate == 0) and animals[turn].step + step >= length_of_map:
                step = length_of_map - animals[turn].step
            animals[turn].move(rotate, step, check_available[1][turn])

            if animals[turn].step == length_of_map:
                elapsed_time = round(Decimal(time.time() - start_time), 3)
                if not check_if_win:
                    winner = turn
                    check_if_win = True
                mark_rank(animals[turn], rank, elapsed_time)
                rank += 1
                score[turn] = elapsed_time

            if check_available[0][0] and check_available[0][1] and check_available[0][2] and check_available[0][3]:
                for i in range(0, 4, 1):
                    if animals[i].step < length_of_map:
                        check_available[0][i] = False
                    else:
                        check_available[0][i] = True
    return winner, score


def draw_rectangle(winner):
    for i in range(16):
        winner.animal.forward(100)
        winner.animal.right(90)


def draw_star(winner):
    for i in range(20):
        winner.animal.forward(100)
        winner.animal.right(144)


def draw_polygon(winner):
    num_sides = 6
    side_length = 70
    angle = 360.0 / num_sides
    for i in range(num_sides * 3):
        winner.animal.forward(side_length)
        winner.animal.right(angle)


def winning_pose(winner):
    winner.animal.penup()
    winner.animal.speed(3)
    winner.animal.left(180)
    winner.animal.forward(400)
    choose_winning_pose = randint(0, 2)
    if choose_winning_pose == 0:
        draw_rectangle(winner)
    elif choose_winning_pose == 1:
        draw_star(winner)
    elif choose_winning_pose == 2:
        draw_polygon(winner)


def begin_match(level, destroy_menu):
    destroy_menu.destroy()
    draw_map(level)
    name, choose, animals = set_up_turtle(level)

    if level == 1: length_to_race = 400
    elif level == 2: length_to_race = 800
    else: length_to_race = 1000

    check_available_to_move = [[0 for i in range(4)] for i in range(3)]
    for i in range(0, 4, 1):
        check_available_to_move[0][i] = False #The first row describe if the animals can move
        check_available_to_move[1][i] = False
        check_available_to_move[2][i] = 0

    winner, score = race(animals, check_available_to_move, length_to_race)
    winning_pose(animals[winner])
    turtle.bye()
    if choose == winner + 1:
        endgame_board(True)
    else:
        endgame_board(False)