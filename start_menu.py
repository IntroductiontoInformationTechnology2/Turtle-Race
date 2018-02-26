from match import begin_match
from winsound import PlaySound, SND_ASYNC, SND_LOOP
from tkinter import Button, Label, Canvas, messagebox, PhotoImage, StringVar, RAISED
import tkinter


def set_pos_start_gui(gui, width_of_menu, height_of_menu):
    """This function is used to set start postition of menu and the size of menu"""
    ws = gui.winfo_screenwidth()
    hs = gui.winfo_screenheight()
    start_pos_x = (ws / 2) - (width_of_menu / 2)
    start_pos_y = (hs / 2) - (height_of_menu / 2)
    gui.geometry('%dx%d+%d+%d' % (width_of_menu, height_of_menu, start_pos_x, start_pos_y))


def choose_level(destroy_menu):
    """This function is used to draw menu and choose size of map"""
    destroy_menu.destroy()
    choose_map = tkinter.Tk()
    choose_map.title("Select Level")

    set_pos_start_gui(choose_map, 750, 450)
    background = Canvas(choose_map, height=750, width=450)
    filename = PhotoImage(file='resources/main_background.png')
    Label(choose_map, image=filename).place(x=0, y=0, relwidth=1, relheight=1)

    text_ask = StringVar()
    text_ask.set("CHOOSE SIZE OF MAP")
    Label(choose_map, textvariable=text_ask, background='light yellow', font=('Kaushan Script', 28), relief=RAISED, cursor='circle').pack()
    Button(choose_map, text="SHORT", command=lambda: begin_match(1, choose_map), height=2, width=14, font=('Kaushan Script', 12), background='light yellow', cursor='circle').pack()
    Button(choose_map, text="MEDIUM", command=lambda: begin_match(2, choose_map), height=2, width=14, font=('Kaushan Script', 12), background='light yellow', cursor='circle').pack()
    Button(choose_map, text="LONG", command=lambda: begin_match(3, choose_map), height=2, width=14, font=('Kaushan Script', 12), background='light yellow', cursor='circle').pack()
    background.pack()
    choose_map.mainloop()


def info():
    """Information about the game"""
    path_info = 'resources/info.txt'
    read_info = open(path_info, 'r')
    messagebox.showinfo("About", read_info.read())
    read_info.close()


def introduction():
    """How to play"""
    path_introduction = 'resources/introduction.txt'
    read_introduction = open(path_introduction, 'r')
    messagebox.showinfo("Introduction", read_introduction.read())
    read_introduction.close()


def draw_menu():
    """Draw main menu"""
    PlaySound('resources/POL-pet-park-short.wav', SND_ASYNC + SND_LOOP)
    menu_gui = tkinter.Tk()
    menu_gui.title("MAIN MENU")
    menu_gui.config(background = 'white')
    set_pos_start_gui(menu_gui, 750, 450)
    background = Canvas(menu_gui, height=750, width=450)
    filename = PhotoImage(file='resources/main_background.png')
    Label(menu_gui, image=filename).place(x=0, y=0, relwidth=1, relheight=1)

    text_welcome = StringVar()
    text_welcome.set("WELCOME TO THE TURTLE RACE")

    Label(menu_gui, textvariable=text_welcome, background='light yellow', font=('Kaushan Script', 28), relief=RAISED, cursor='circle').pack()
    Button(menu_gui, text='START', command=lambda: choose_level(menu_gui), height=2, width=14, font=('Kaushan Script', 12), background='light yellow', cursor='circle').pack()
    #Button(menu_gui, text='SETTINGS', height=1, width=14, font=('Kaushan Script', 12), background='light yellow', cursor='circle').pack()
    Button(menu_gui, text='INTRODUCTION', command=lambda: introduction(), height=2, width=14, font=('Kaushan Script', 12), background='light yellow', cursor='circle').pack()
    Button(menu_gui, text='ABOUT', command=lambda: info(),height = 2, width=14, font=('Kaushan Script', 12), background='light yellow', cursor='circle').pack()
    ##99e6ff
    background.pack()
    menu_gui.mainloop()

