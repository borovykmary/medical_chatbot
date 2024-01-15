# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Chatbot")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "./asking_for_name.yml",
    "./asking_for_symptoms.yml",
    "./asking_for_doctor.yml"
)
print("🪴 Hi")
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
