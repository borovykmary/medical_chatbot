import tkinter as tk
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.chat_page import MainPage


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("medical chatbot test")

        self.geometry("900x600")
        self.login_page = LoginPage(self)
        self.register_page = RegisterPage(self)
        self.main_page = MainPage(self)

        self.login_page.grid(row=0, column=0, sticky="nsew")
        self.register_page.grid(row=0, column=0, sticky="nsew")
        self.main_page.grid(row=0, column=0, sticky="nsew")

        self.show_login_page()

    def show_login_page(self, event=None):
        self.login_page.tkraise()

    def show_register_page(self, event=None):
        self.register_page.tkraise()

    def show_main_page(self):
        self.main_page.tkraise()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
