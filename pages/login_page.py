import tkinter as tk
from res.custom_widgets import RoundedButton
from firebase_admin import auth
from tkinter import messagebox


class LoginPage(tk.Frame):
    def __init__(self, master=None, auth=None, db=None, **kwargs):
        super().__init__(master, **kwargs)
        self.auth = auth
        self.db = db

        self.grid_columnconfigure(0, weight=1)  # Configure the column weights
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        for i in range(7):
            self.grid_rowconfigure(i, weight=1, minsize=50)

        self.login_label = tk.Label(self, text="Log in", font=("Changa-SemiBold", 20))
        self.email_label = tk.Label(self, text="Email:", font=("Changa", 12), fg="#718096")
        self.password_label = tk.Label(self, text="Password:", font=("Changa", 12), fg="#718096")
        self.email_entry = tk.Entry(self, font=("Changa", 12), fg="#080F17", width=35)
        self.password_entry = tk.Entry(self, show="*", font=("Changa", 12), fg="#080F17", width=35)
        self.login_button = RoundedButton(self, text="Login", command=self.login, font=("Changa", 12), fg="#F7FAFC",
                                          bg="#080F17")

        # Create a Frame to group the register_text and register_button
        self.register_frame = tk.Frame(self)
        self.register_text = tk.Label(self.register_frame, text="Don't have an account yet?", font=("Changa", 12),
                                      fg="#718096")
        self.register_button = tk.Label(self.register_frame, text="Register", font=("Changa", 12), fg="#080F17",
                                        cursor="hand2")
        self.register_button.bind("<Button-1>", self.master.show_register_page)

        # Load the image
        self.image = tk.PhotoImage(
            file="/Users/marynaborovyk/Desktop/pythonProject/res/drawable/bg_login.png")
        self.image_label = tk.Label(self, image=self.image)

        self.login_label.grid(row=0, column=1, pady=5, padx=10, sticky="w")
        self.email_label.grid(row=2, column=1, pady=5, padx=10, sticky="w")
        self.email_entry.grid(row=3, column=1, pady=5, padx=10)
        self.password_label.grid(row=4, column=1, pady=5, padx=10, sticky="w")
        self.password_entry.grid(row=5, column=1, pady=5, padx=10)
        self.login_button.grid(row=6, column=1, columnspan=2, sticky="w", pady=5, padx=10)

        # Place the register_text and register_button in the register_frame
        self.register_text.grid(row=0, column=0)
        self.register_button.grid(row=0, column=1)

        # Place the register_frame in the grid
        self.register_frame.grid(row=1, column=1, pady=5, padx=10, sticky="w")
        self.image_label.grid(row=0, column=3, rowspan=7, sticky="nsew")

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        try:
            user = auth.get_user_by_email(email)
            self.master.show_main_page()
        except auth.AuthError as e:
            messagebox.showerror("Login Error", str(e))
