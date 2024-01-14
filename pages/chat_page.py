import functools
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


class MainPage(tk.Frame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.height = 600
        self.width = 900

        self.bg_image = ctk.CTkImage(Image.open("/Users/marynaborovyk/Desktop/python_app/res/drawable/chat_bg_updated.png"),
                                     size=(self.width, self.height))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image,text="")
        self.bg_image_label.pack(fill="both", expand=True)

        self.chat_number_label = tk.Label(self.bg_image_label, text="Chat Number: 1", font=("Changa", 12))
        self.chat_number_label.place(relx=0.245, rely=0.03, relwidth=0.73, relheight=0.05)

        self.chat_history = tk.Text(self.bg_image_label)
        self.chat_history.place(relx=0.245, rely=0.15, relwidth=0.73, relheight=0.7)

        self.message_entry = tk.Entry(self.bg_image_label)
        self.message_entry.place(relx=0.245, rely=0.89, relwidth=0.73, relheight=0.05)

        self.send_button = tk.Button(self.bg_image_label, text="Send", command=self.send_message,
                                          bg="#718096", font=("Changa-SemiBold", 12))

        self.logout_button = tk.Button(self.bg_image_label, text="Logout", command=self.logout,
                                       bg="#718096", font=("Changa-SemiBold", 12))
        self.logout_button.place(relx=0.01, rely=0.1, relwidth=0.2, relheight=0.05)

        self.new_chat_button = tk.Button(self.bg_image_label, text="New Chat", command=self.new_chat,
                                         bg="#718096", font=("Changa-SemiBold", 12))
        self.new_chat_button.place(relx=0.01, rely=0.2, relwidth=0.2, relheight=0.05)
        self.chat_boxes = []
        for i in range(4):
            chat_box = tk.Button(self.bg_image_label, text=f"Chat {i + 1}",
                                command=functools.partial(self.switch_chat, i + 1),
                                bg="#718096", font=("Changa", 12))
            chat_box.place(relx=0.01, rely=0.3 + i * 0.05, relwidth=0.2, relheight=0.05)
            self.chat_boxes.append(chat_box)

        self.send_button.place(relx=0.9, rely=0.89, relwidth=0.08, relheight=0.05)
        self.bot_messages = ["How are you?", "What is your favourite color?", "What is your age?"]
        self.bot_message_index = 0

        self.bot_chat(self.bot_messages[self.bot_message_index])
        self.current_y = 0.07

    def create_message_bubble(self, message, message_type, container):
        bubble = ctk.CTkFrame(container, width=340, bg_color="#718096")
        bubble.place(relx=0.05 if message_type == "bot" else 0.94, rely=self.current_y, anchor="w" if message_type == "bot" else "e")

        message_label = ctk.CTkLabel(bubble, text=message, wraplength=260, bg_color="#718096", corner_radius=8, text_color="white", font=("Changa", 12))
        message_label.pack()

    def animate_chat(self, message, message_type):
        self.create_message_bubble(message, message_type, self.chat_history)
        self.current_y += 0.06

    def send_message(self):
        message = self.message_entry.get()
        self.message_entry.delete(0, tk.END)
        self.animate_chat(message, "user")

        self.bot_message_index += 1
        if self.bot_message_index < len(self.bot_messages):
            self.bot_chat(self.bot_messages[self.bot_message_index])

    def bot_chat(self, message):
        self.after(500, lambda: self.animate_chat(message, "bot"))

    def logout(self):
        self.master.show_login_page()

    def new_chat(self):
        pass

    def switch_chat(self, chat_number):
        pass