import tkinter as tk
from res.custom_widgets import RoundedButton
from firebase_admin import auth
from tkinter import messagebox


class RegisterPage(tk.Frame):
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

        self.register_label = tk.Label(self, text="Register", font=("Changa-SemiBold", 20))
        self.email_label = tk.Label(self, text="Email:", font=("Changa", 12), fg="#718096")
        self.password_label = tk.Label(self, text="Password:", font=("Changa", 12), fg="#718096")
        self.email_entry = tk.Entry(self, font=("Changa", 12), fg="#080F17", width=35)
        self.password_entry = tk.Entry(self, show="*", font=("Changa", 12), fg="#080F17", width=35)
        self.register_button = RoundedButton(self, text="Register", command=self.register, font=("Changa", 12),
                                             fg="#F7FAFC",
                                             bg="#080F17")

        # Create a Frame to group the login_text and login_button
        self.login_frame = tk.Frame(self)
        self.login_text = tk.Label(self.login_frame, text="Already have an account?", font=("Changa", 12), fg="#718096")
        self.login_button = tk.Label(self.login_frame, text="Login", font=("Changa", 12), fg="#080F17", cursor="hand2")
        self.login_button.bind("<Button-1>", self.master.show_login_page)

        # Load the image
        self.image = tk.PhotoImage(
            file="/Users/marynaborovyk/Desktop/pythonProject/res/drawable/bg_login.png")
        self.image_label = tk.Label(self, image=self.image)

        self.register_label.grid(row=0, column=1, pady=5, padx=10, sticky="w")
        self.email_label.grid(row=2, column=1, pady=5, padx=10, sticky="w")
        self.email_entry.grid(row=3, column=1, pady=5, padx=10)
        self.password_label.grid(row=4, column=1, pady=5, padx=10, sticky="w")
        self.password_entry.grid(row=5, column=1, pady=5, padx=10)
        self.register_button.grid(row=6, column=1, columnspan=2, sticky="w", pady=5, padx=10)

        # Place the login_text and login_button in the login_frame
        self.login_text.grid(row=0, column=0)
        self.login_button.grid(row=0, column=1)

        # Place the login_frame in the grid
        self.login_frame.grid(row=1, column=1, pady=5, padx=10, sticky="w")
        self.image_label.grid(row=0, column=3, rowspan=7, sticky="nsew")

    def register(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        try:
            user = auth.create_user(email=email, password=password)
            messagebox.showinfo("Registration", "Registration successful!")

            self.db.collection('users').document(user.uid).set({
                'email': email
            })
            self.show_login_page()

        except ValueError as e:
            messagebox.showerror("Registration Error", str(e))
