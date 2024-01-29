from ttc import Chatbot, Context, download_nltk_data

# Only needs to be run once (can be removed after first run)
#download_nltk_data()

# Creating the context
ctx = Context()

# Initializing the chatbot
#chatbot = Chatbot()

chatbot = Chatbot(
    path="brain",
    learn=True,
    min_score=0.5,
    score_threshold=0.5,
    mesh_association=0.5,
)
"""
demonstration code of chatbot before actual implementation

talk = True

while talk:
    msg = input("You: ")

    if msg == "s":
        talk = False
    else:
        # Getting the response
        resp = chatbot.respond(ctx, msg)

        # Saving the response to the context
        ctx.save_resp(resp)

        print(f"Thomas: {resp}")

# Saving the chatbot data
chatbot.save_data()
"""
