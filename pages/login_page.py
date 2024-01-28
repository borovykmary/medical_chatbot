import hashlib
import mysql.connector
import tkinter as tk
from res.custom_widgets import RoundedButton
from tkinter import messagebox


class LoginPage(tk.Frame):
    def __init__(self, master=None, db=None, **kwargs):
        super().__init__(master, **kwargs)
        self.db = db

        # design of widgets
        self.login_label = tk.Label(self, text="Log in", font=("Changa-SemiBold", 20))
        self.email_label = tk.Label(self, text="Email:", font=("Changa", 12), fg="#718096")
        self.password_label = tk.Label(self, text="Password:", font=("Changa", 12), fg="#718096")
        self.email_entry = tk.Entry(self, font=("Changa", 12), fg="#080F17", width=35)
        self.password_entry = tk.Entry(self, show="*", font=("Changa", 12), fg="#080F17", width=35)
        self.login_button = RoundedButton(self, text="Login", command=self.login, font=("Changa", 12), fg="#F7FAFC",
                                          bg="#080F17")
        self.register_frame = tk.Frame(self, width=400, height=50)
        self.register_text = tk.Label(self.register_frame, text="Don't have an account yet?", font=("Changa", 12),
                                      fg="#718096")
        self.register_button = tk.Label(self.register_frame, text="Create now", font=("Changa", 12), fg="#080F17",
                                        cursor="hand2")
        self.register_button.bind("<Button-1>", self.master.show_register_page)
        self.image = tk.PhotoImage(
            file="/Users/marynaborovyk/Desktop/python_app/res/drawable/bg_login.png")
        self.image_label = tk.Label(self, image=self.image)

        # placement of widgets
        self.login_label.place(relx=0.1, rely=0.1)
        self.register_frame.place(relx=0.1, rely=0.2)
        self.register_text.place(relx=0, rely=0)
        self.register_button.place(relx=0.4, rely=0)
        self.email_label.place(relx=0.1, rely=0.3)
        self.email_entry.place(relx=0.1, rely=0.4)
        self.password_label.place(relx=0.1, rely=0.5)
        self.password_entry.place(relx=0.1, rely=0.6)
        self.login_button.place(relx=0.1, rely=0.8)
        self.image_label.place(relx=0.55, rely=0.1)

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Flover18",
            database="register"
        )
        self.cursor = self.conn.cursor()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        self.cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = self.cursor.fetchone()

        if user is None:
            messagebox.showerror("Login Error", "User not found")
        elif user[2] != hashed_password:
            messagebox.showerror("Login Error", "Incorrect password")
        else:
            self.master.show_main_page()
