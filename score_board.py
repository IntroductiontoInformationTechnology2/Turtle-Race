from winsound import PlaySound, SND_ASYNC, SND_LOOP
from tkinter import Button, Label, Canvas, messagebox, PhotoImage, StringVar, RAISED
import tkinter


def set_pos_start_gui(gui, width_of_menu, height_of_menu):
    ws = gui.winfo_screenwidth()
    hs = gui.winfo_screenheight()
    start_pos_x = (ws / 2) - (width_of_menu / 2)
    start_pos_y = (hs / 2) - (height_of_menu / 2)
    gui.geometry('%dx%d+%d+%d' % (width_of_menu, height_of_menu, start_pos_x, start_pos_y))


def exit_game():
    import sys
    sys.exit()


def endgame_board(result):
    result_menu = tkinter.Tk()
    result_menu.title("RESULT")
    result_menu.config(background='white')
    set_pos_start_gui(result_menu, 750, 450)
    background = Canvas(result_menu, height=750, width=450)
    filename = PhotoImage(file='resources/main_background.png')
    Label(result_menu, image=filename).place(x=0, y=0, relwidth=1, relheight=1)
    result_text = StringVar()
    if result:
        result_text.set("YOU WIN")
    else:
        result_text.set("YOU LOSE")
    Label(result_menu, textvariable=result_text, font=('Kaushan Script', 50), background='light yellow', relief=RAISED, cursor='circle').pack()
    Button(result_menu, text='SCOREBOARD', height=2, width=14, font=('Kaushan Script', 12), background='light yellow', cursor='circle').pack()
    Button(result_menu, text='EXIT', command=exit_game, height=2, width=14, font=('Kaushan Script', 12), background='light yellow', cursor='circle').pack()
    background.pack()
    result_menu.mainloop()
