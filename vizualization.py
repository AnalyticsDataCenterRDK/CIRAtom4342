import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np


#столбчатая диаграмма
def vizual():
    vizualization_root = tk.Tk()
    vizualization_root.geometry("1000x500")
    vizualization_root.title("C.I.R Atom Vizualization")

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    x = np.array(['A', 'B', 'C', 'D', 'E'])
    y = np.random.randint(0, 10, size=5)

    ax.bar(x, y)

    canvas = FigureCanvasTkAgg(fig, master=vizualization_root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


#круговая диаграмма
def vizual_pie():
    root = tk.Tk()
    root.geometry('1000x500')
    root.title("C.I.R Atom Vizualization")

    labels = ['A', 'B', 'C', 'D']
    values = [35, 25, 25, 15]

    # Создание графика
    fig = Figure(figsize=(5, 4), dpi=100)
    fig.suptitle('Пример круговой диаграммы')
    ax = fig.add_subplot(111)
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)


    # Создание виджета Canvas для отображения графика в tkinter окне
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    # Размещение виджета Canvas в окне tkinter
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)