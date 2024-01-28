import tkinter as tk
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.chat_page import MainPage


class Application(tk.Tk):
    """
    Main application class
    Attributes:
        login_page(LoginPage): login page
        register_page(RegisterPage): register page
        main_page(MainPage): main page
    Methods:
        show_login_page(self, event=None): shows login page
        show_register_page(self, event=None): shows register page
        show_main_page(self): shows main page
    """
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
        """
        function to show login page
        """
        self.login_page.tkraise()

    def show_register_page(self, event=None):
        """
        function to show register page
        """
        self.register_page.tkraise()

    def show_main_page(self):
        """
        function to show main page
        """
        self.main_page.tkraise()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
