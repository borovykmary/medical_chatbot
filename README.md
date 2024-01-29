# Medical Chatbot

This project is a medical chatbot application developed in Python. It uses the Tkinter library for the graphical user interface and MySQL for database management. The application allows users to register, login, and interact with the chatbot.

## Project Structure

The project is structured into several Python files, each serving a specific purpose:

- `main.py`: This is the entry point of the application. It initializes and manages the application's main window and the transition between different pages (login, register, main).

- `pages/login_page.py`: This file contains the `LoginPage` class, which represents the login page of the application. It handles user authentication.

- `pages/register_page.py`: This file contains the `RegisterPage` class, which represents the registration page of the application. It handles user registration.

- `pages/chat_page.py`: This file contains the `MainPage` class, which represents the main page of the application where the user interacts with the chatbot.

- `convert_to_pdf.py`: This file contains a function to convert patient's data to a PDF file.

## Requirements

- Python
- Tkinter
- MySQL
- PyLaTeX

## Setup

To run this project, you need to have Python version>3.9. After cloning the project, install the necessary dependencies by running `pip install -r requirements.txt` in your terminal.

## Usage

To start the application, navigate to the project directory in your terminal and run `python main.py`.

