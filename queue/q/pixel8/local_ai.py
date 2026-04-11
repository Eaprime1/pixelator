from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf") # Downloads model on first run
with model.chat_session():
    print(model.generate("How do I use Python?"))
