from cobe import brain
import random

brain = brain.Brain("brain.db")

print("Welcome to the AI chatbot, powered by COBE! Ask me anything! I'll try my best to answer.")
while True:
    user_input = input("You: ")
    response = []
    for i in range(0, 2):
      print("Thinking... " + str(i+1) + "/2")
      response.append(brain.reply(user_input, max_len=300))
    
    response = random.choice(response) 
    print("AI: " + response)
