import cobe
import random
import nltk
from cobe import brain

nltk.download('brown')

print("Training AI...")
brain = brain.Brain("brain.db")

print("Loading corpus...")
corpus = nltk.corpus.brownA.sents()
for sentence in corpus:
    text = " ".join(sentence)
    import re
    text = re.sub(r'(?m)^\s*\n', '', text) # remove empty lines
    text = re.sub(r'\[[^\]]+\]', '', text) # remove metadata
    text = re.sub(r'\n\n+', '\n', text) # remove extra line breaks
    print("Training on: " + text)
    brain.learn(text)

print("Training complete!")

brain.save()

#Detect CTRL+C and save all the learnt data.
import signal, sys
def signal_handler(signal, frame):
    print("Saving...")
    brain.save()
    print("Saved!")
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
