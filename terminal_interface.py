import os, sys, json, csv
from functions import *
from print_color import print
from llama_cpp import Llama

#Set model direction in model_path=""


llm = Llama(model_path="" , n_gpu_layers=-1, n_ctx = 2048, n_threads=12)

#LLM Selection + History init
llm_name = char_selector()
    
#Load existing history
history_path = os.path.join("history", f'history_{llm_name}.csv')
try:
    with open(history_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        history_dict = list(reader)
        for key in history_dict:
            history = ''
            history = history + prompter(key, history_dict[key])
except FileNotFoundError:
    history = ''
    history_dict = []

#Chat
while True:
    
    user_message = input("User:> ")
    if user_message == 'exit':
        sys.exit(0)  
    history, history_dict = history_update_print('user', history, history_dict, user_message)

    output = llm(prompt=promp_generator(history),
                max_tokens=2048,
                stop="<|im_end|>",
                temperature=0.81,
                top_p=1.0,
                top_k=0,
                min_p=0.1,
                repeat_penalty=1.0)  
    assistant_message= output["choices"][0]["text"]

    history, history_dict = history_update_print('assistant', history, history_dict, assistant_message, True, llm_name)
    print(assistant_message, tag=llm_name, tag_color='magenta', color='cyan')