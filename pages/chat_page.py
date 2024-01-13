import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


class MainPage(tk.Frame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.height = 500
        self.width = 700

        self.bg_image = ctk.CTkImage(Image.open("/Users/marynaborovyk/Desktop/pythonProject/res/drawable/chat_bg.png"),
                                     size=(self.width, self.height))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image,text="")
        self.bg_image_label.pack(fill="both", expand=True)

        self.button1 = tk.Button(self, text="Button 1")
        self.button2 = tk.Button(self, text="Button 2")
        self.button3 = tk.Button(self, text="Button 3")
        self.button4 = tk.Button(self, text="Button 4")

        self.button1.place(x=20, y=20)
        self.button2.place(x=20, y=60)
        self.button3.place(x=20, y=100)
        self.button4.place(x=20, y=140)