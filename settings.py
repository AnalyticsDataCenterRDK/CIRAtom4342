from tkinter import ttk
from tkinter import *


def setting():
    root = Tk()

    root.geometry("1000x500")
    root.title("C.I.R Atom Analytics Settings")

    mainmenu = Menu(root)
    root.config(menu=mainmenu)

    settings = Menu(mainmenu, tearoff=0)
    settings.add_command(label="светлая тема")
    settings.add_command(label="темная тема")
    settings.add_command(label="желтая тема")
    settings.add_command(label="оранжевая тема ")
    settings.add_command(label="фиолетовая тема")
    settings.add_command(label="коричневая тема")
    settings.add_command(label="красная тема")
    settings.add_command(label="синяя тема")
    settings.add_command(label="голубая тема")
    settings.add_command(label="зеленая тема")


    mainmenu.add_cascade(label="Поменять фон в программы", menu=settings)
    mainmenu.add_cascade(label="Поменять шрифт программы")