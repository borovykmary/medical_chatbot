import tkinter as tk
from res.custom_widgets import RoundedButton
from firebase_admin import auth
from tkinter import messagebox


class RegisterPage(tk.Frame):
    def __init__(self, master=None, auth=None, db=None, **kwargs):
        super().__init__(master, **kwargs)
        self.auth = auth
        self.db = db

         # design of widgets
        self.register_label = tk.Label(self, text="Register", font=("Changa-SemiBold", 20))
        self.email_label = tk.Label(self, text="Email:", font=("Changa", 12), fg="#718096")
        self.password_label = tk.Label(self, text="Password:", font=("Changa", 12), fg="#718096")
        self.email_entry = tk.Entry(self, font=("Changa", 12), fg="#080F17", width=35)
        self.password_entry = tk.Entry(self, show="*", font=("Changa", 12), fg="#080F17", width=35)
        self.register_button = RoundedButton(self, text="Register", command=self.register, font=("Changa", 12),
                                             fg="#F7FAFC",
                                             bg="#080F17")
        self.login_frame = tk.Frame(self, width=400, height=50)
        self.login_text = tk.Label(self.login_frame, text="Already have an account?", font=("Changa", 12), fg="#718096")
        self.login_button = tk.Label(self.login_frame, text="Login", font=("Changa", 12), fg="#080F17", cursor="hand2")
        self.login_button.bind("<Button-1>", self.master.show_login_page)
        self.image = tk.PhotoImage(
            file="/Users/marynaborovyk/Desktop/pythonProject/res/drawable/bg_login.png")
        self.image_label = tk.Label(self, image=self.image)

        # placement of widgets
        self.register_label.place(relx=0.1, rely=0.1)
        self.login_frame.place(relx=0.1, rely=0.2)
        self.login_text.place(relx=0, rely=0)
        self.login_button.place(relx=0.4, rely=0)
        self.email_label.place(relx=0.1, rely=0.3)
        self.email_entry.place(relx=0.1, rely=0.4)
        self.password_label.place(relx=0.1, rely=0.5)
        self.password_entry.place(relx=0.1, rely=0.6)
        self.register_button.place(relx=0.1, rely=0.8)
        self.image_label.place(relx=0.55, rely=0.1)

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
