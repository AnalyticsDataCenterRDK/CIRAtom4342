from source_integration import integration
from vizualization import vizual_pie
from analytics import analytics
from history import history
from sources import source
from contacts import contact
from data_upload import data_upload
from processing import process
from settings import setting
from tkinter import *

root = Tk()

root.geometry("1000x500")
root.title("C.I.R Atom Analytics")


def menu():
    mainmenu = Menu(root)
    root.config(menu=mainmenu)

    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Загрузка данных", command=data_upload)
    filemenu.add_command(label="Предоброботка данных", command=process)
    filemenu.add_command(label="Визуализация", command=vizual_pie)
    filemenu.add_command(label="Аналитика", command=analytics)
    filemenu.add_command(label="Источники", command=source)
    filemenu.add_command(label="История", command=history)
    filemenu.add_command(label="Контакты", command=contact)
    filemenu.add_command(label="Интеграция с источниками", command=integration)

    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="Помощь")
    helpmenu.add_command(label="О программе")

    settings = Menu(mainmenu, tearoff=0)
    settings.add_command(label="Настройки", command=setting)

    mainmenu.add_cascade(label="Функции",menu=filemenu)
    mainmenu.add_cascade(label="Справка",menu=helpmenu)
    mainmenu.add_cascade(label="Настройки", menu=settings)


menu()
root.mainloop()