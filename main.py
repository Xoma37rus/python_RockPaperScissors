import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pygame
from pygame import *
from PIL import Image, ImageTk
import random as rdm
import os

IMG_URL = os.getcwd()

class Game(Frame):
    def __init__(self, root, IMG_URL):
        super(Game, self).__init__(root)
        self.startUI(IMG_URL)

    def startUI(self, img_url):
        buton1 = Button(root, text="Камень", font=("Times New Roman", 15), command=lambda x=1: self.boton_click(x,IMG_URL))
        buton2 = Button(root, text="Ножницы", font=("Times New Roman", 15), command=lambda x=2: self.boton_click(x, IMG_URL))
        buton3 = Button(root, text="Бумага", font=("Times New Roman", 15), command=lambda x=3: self.boton_click(x, IMG_URL))
        buton4 = Button(root, text="О авторе", font=("Times New Roman", 15), command=lambda x=4: self.boton_click(x, IMG_URL))

        buton1.place(x=10, y=100, width=120, height=50)
        buton2.place(x=155, y=100, width=120, height=50)
        buton3.place(x=300, y=100, width=120, height=50)
        buton4.place(x=10, y=155, width=120, height=50)

        self.lbl = Label(root, text="Начало игры!", bg="#FFF",
                         font=("Times New Roman", 21, "bold"))
        self.lbl.place(x=175, y=25)

        self.win = self.drow = self.lose = 0

        self.lbl2 = Label(root, justify="left", font=("Times New Roman", 13),text=f"Побед: {self.win}\nПроигрышей:" f" {self.lose}\nНичьи́х: {self.drow} ",
                          bg="#FFF")
        self.lbl2.place(x=5, y=5)

        self.python_img = ImageTk.PhotoImage(Image.open(os.path.abspath(img_url+'\img\help.png')))

        self.image_label = tk.Label(root, image=self.python_img, bg="#FFF")

        self.image_label.place(x=155, y=215, width=190, height=194)

        self.ant_label = tk.Label(root, justify="center", font=("Times New Roman", 10), text=f'ИИ: Нажми на кнопку!',
                                  bg="#FFF")
        self.ant_label.place(x=200, y=435)

    def boton_click(self, choise, img_url):
        comp_choise = rdm.randint(1, 3)
        self.after(1, self.image_label.destroy)
        self.after(1, self.ant_label.destroy)
        def ans_bot():
            if comp_choise == 1:
                self.python_img = ImageTk.PhotoImage(Image.open(img_url + '\img\stone.jpg'))
                self.image_label = tk.Label(root, image=self.python_img, bg="#FFF")
                self.image_label.place(x=155, y=215)
                self.ant_label = tk.Label(root, justify="center", font=("Times New Roman", 10),
                                          text=f'ИИ: а у меня камень.', bg="#FFF")
                self.ant_label.place(x=200, y=435)

            elif comp_choise == 2:
                self.python_img = ImageTk.PhotoImage(Image.open(img_url + '\img\cut.jpg'))
                self.image_label = tk.Label(root, image=self.python_img, bg="#FFF")
                self.image_label.place(x=155, y=215)
                self.ant_label = tk.Label(root, justify="center", font=("Times New Roman", 10),
                                          text=f'ИИ: а у меня ножницы.', bg="#FFF")
                self.ant_label.place(x=200, y=435)

            elif comp_choise == 3:
                self.python_img = ImageTk.PhotoImage(Image.open(img_url + '\img\paper.jpg'))
                self.image_label = tk.Label(root, image=self.python_img, bg="#FFF")
                self.image_label.place(x=155, y=215)
                self.ant_label = tk.Label(root, justify="center", font=("Times New Roman", 10),
                                          text=f'ИИ: а у меня бумага.', bg="#FFF")
                self.ant_label.place(x=195, y=435)

        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(font=("Times New Roman", 21, "bold"), text="Ничья")
            ans_bot()
        elif choise == 1 and comp_choise == 2 \
                or choise == 2 and comp_choise == 3 \
                or choise == 3 and comp_choise == 1:
            self.win += 1
            self.lbl.configure(font=("Times New Roman", 21, "bold"), text="Победа")
            ans_bot()
        elif choise == 4:
            self.lbl.configure(justify="left", font=("Times New Roman", 14, "bold"),text="Автор - Груздев А.С. \nEmail: artemgruzdev@gmail.com\nАвтор изображений: Freepik")
            self.lbl.place(x=175, y=5)
            self.python_img = ImageTk.PhotoImage(Image.open(img_url + '\img\help.png'))
            self.image_label = tk.Label(root, image=self.python_img, bg="#FFF")
            self.image_label.place(x=155, y=215, width=190, height=194)
            self.ant_label = tk.Label(root, justify="center", font=("Times New Roman", 10), text=f'ИИ: О создатель!!!', bg="#FFF")
            self.ant_label.place(x=200, y=435)
        else:
            self.lose += 1
            self.lbl.configure(font=("Times New Roman", 21, "bold"), text="Проигрыш")
            ans_bot()

        self.lbl2.configure(text=f"Побед: {self.win}\nПроигрышей:"
                                 f" {self.lose}\nНичьи́х: {self.drow}")

        del comp_choise

def on_closing(): #Функция подстраховка случайного закрытия.
    if messagebox.askokcancel("Выход из игры: Камень, ножницы, бумага ", 'Ну что выходим?'):
        root.destroy()

if __name__ == '__main__':
    root = Tk()
    pygame.init()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.geometry("500x460+200+200")
    root.iconbitmap(IMG_URL + '\img\icon.ico')
    root.title("Камень, ножницы, бумага")
    root.resizable(False, False)
    root["bg"] = "#FFF"
    Game(root, IMG_URL).pack()
    frame_game = Canvas(root, width=195, height=240, highlightthickness=0)
    frame_game.pack(pady=215)



    root.mainloop()