import functools
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


from bot import ctx
from bot import chatbot

from convert_to_pdf import convert_to_pdf


class MainPage(tk.Frame):
    """
    Main "Chat" page of the medical_bot app

    Attributes:
        bg_image(Image): background image
        bg_image_label(Image): background image label
        chat_number_label(tk.Label): label with chat number
        chat_history(tk.Text): chat history
        message_entry(tk.Entry): message entry
        send_button(tk.Button): send button
        logout_button(tk.Button): logout button
        new_chat_button(tk.Button): new chat button
        chat_boxes(list): list of chat boxes
        current_chat(int): current chat
        greetings(str): greeting message
        ask_for_symptoms(str): message asking for symptoms
        calm(str): message calming patient
        user_answers(list): list of user's answers
        bot_messages(list): list of bot's messages
        bot_message_index(int): index of bot's message
        input_name(str): input name
        input_symptoms(str): input symptoms
        current_y(int): current y coordinate

    Methods:
        create_message_bubble(self, message, message_type, container): creates a message bubble
        animate_chat(self, message, message_type): animates chat
        send_message(self): sends message
        bot_chat(self, message): bot's message
        logout(self): logout
        new_chat(self): creates a new chat
        switch_chat(self, current_chat): switches between chats
        save_user_answers(self, answer): saves user's answers
    """

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

        self.chat_history = tk.Frame(self.bg_image_label, bg='white')
        self.chat_history.place(relx=0.245, rely=0.15, relwidth=0.73, relheight=0.7)

        self.message_entry = tk.Entry(self.bg_image_label)
        self.message_entry.place(relx=0.245, rely=0.89, relwidth=0.73, relheight=0.05)

        self.send_button = tk.Button(self.bg_image_label, text="Send", command=self.send_message,
                                          bg="#718096", font=("Changa-SemiBold", 12))

        self.logout_button = tk.Button(self.bg_image_label, text="Logout", command=self.logout,
                                       bg="#718096", font=("Changa-SemiBold", 12))
        self.logout_button.place(relx=0.014, rely=0.1, relwidth=0.215, relheight=0.05)

        self.new_chat_button = tk.Button(self.bg_image_label, text="New Chat", command=self.new_chat,
                                         bg="#718096", font=("Changa-SemiBold", 12))
        self.new_chat_button.place(relx=0.014, rely=0.2, relwidth=0.215, relheight=0.05)
        self.chat_boxes = []
        for i in range(1):
            chat_box = tk.Button(self.bg_image_label, text=f"Chat {i + 1}",
                                command=functools.partial(self.switch_chat, i + 1),
                                bg="#718096", font=("Changa", 12))
            chat_box.place(relx=0.014, rely=0.3 + i * 0.05, relwidth=0.215, relheight=0.05)
            self.chat_boxes.append(chat_box)
        self.current_chat = 1
        self.send_button.place(relx=0.9, rely=0.89, relwidth=0.08, relheight=0.05)

        self.greetings = "Greetings patient, welcome to the queue of our clinic. Could you please share your name?"
        self.ask_for_symptoms = "What brings you here? What are your symptoms?"

        self.calm = "It might be though - waiting, maybe chatting with our bot will make it more pleasant."
        self.start_chat = "Say something to start the conversation with the MM-bot."
        self.user_answers = []

        self.bot_messages = [self.greetings, self.ask_for_symptoms, self.calm, self.start_chat]
        self.bot_message_index = 0

        self.bot_chat(self.bot_messages[self.bot_message_index])
        self.current_y = 0.07

    def create_message_bubble(self, message, message_type, container):
        """
        function to create a message bubble
        Args:
            message(str): message
            message_type(str): message type
            container(tk.Frame): container
        Returns:
            bubble(tk.Frame): message bubble
        """
        bubble = ctk.CTkFrame(container, width=340, bg_color="#718096")
        bubble.place(relx=0.05 if message_type == "bot" else 0.94, rely=self.current_y, anchor="w" if message_type == "bot" else "e")

        message_label = ctk.CTkLabel(bubble, text=message, wraplength=260, bg_color="#718096", corner_radius=8, text_color="white", font=("Changa", 12))
        message_label.pack()

        return bubble

    def animate_chat(self, message, message_type):
        """
        function to animate chat
        Args:
            message(str): message
            message_type(str): message type
        Returns:
            None
        """
        self.create_message_bubble(message, message_type, self.chat_history)
        self.current_y += 0.06


    def send_message(self):
        """
        function to send message
        Args:
            None
        Returns:
            None
        """
        message = self.message_entry.get()
        self.message_entry.delete(0, tk.END)
        self.animate_chat(message, "user")

        # save user's answer
        self.save_user_answers(message)

        if self.bot_message_index < len(self.bot_messages) - 1:
            self.bot_message_index += 1
            self.bot_chat(self.bot_messages[self.bot_message_index])
        else:
            resp = chatbot.respond(ctx, message)
            self.bot_chat(resp)

    def bot_chat(self, message):
        """
        function to animate bot's chat
        Args:
            message(str): message
        Returns:
            None
        """
        self.after(500, lambda: self.animate_chat(message, "bot"))

    def logout(self):
        """
        function to log out
        Args:
            None
        Returns:
            None
        """
        self.master.show_login_page()

    def new_chat(self):
        """
        function to create a new chat
        Args:
            None
        Returns:
            None
        """
        self.current_chat += 1

        new_chat_box = tk.Button(self.bg_image_label, text=f"Chat {self.current_chat}",
                                 command=functools.partial(self.switch_chat, self.current_chat),
                                 bg="#718096", font=("Changa", 12))

        new_chat_box.place(relx=0.014, rely=0.3 + (self.current_chat - 1) * 0.05, relwidth=0.215, relheight=0.05)
        self.chat_boxes.append(new_chat_box)

    def switch_chat(self, current_chat):
        """
        example function to switch between chats
        Args:
            current_chat: chat number
        Returns:
            None
        """
        print(f"Switching to chat {current_chat}")
        self.current_chat = current_chat



    def save_user_answers(self, answer):
        """
        function to save user's answers
        Args:
            answer(str): answer
        Returns:
            None
        """
        if len(self.user_answers) < 2:
            self.user_answers.append(answer)
            if len(self.user_answers) == 1:
                self.input_name = self.user_answers[0]
            elif len(self.user_answers) == 2:
                self.input_symptoms = self.user_answers[1]
                convert_to_pdf(self.user_answers)