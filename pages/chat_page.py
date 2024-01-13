import tkinter as tk
import customtkinter as ctk
from PIL import Image


class MainPage(tk.Frame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.height = 500
        self.width = 700

        self.bg_image = ctk.CTkImage(Image.open("/Users/marynaborovyk/Desktop/pythonProject/res/drawable/chat_bg.png"),
                                     size=(self.width, self.height))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0, sticky="nsew")


