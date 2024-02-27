#For the future.
import os, csv
BASE_DIR = os.getcwd()

def char_selector():
    folder_path = "\history"
    extension = ".csv"
    shared_string = "history_"

    files = [file for file in os.listdir(BASE_DIR + folder_path) if file.endswith(extension)]
    if not files:
        choice_new = input("Provide a name for the new Char:")
        return choice_new

    print("Available chars:")
    for i, file in enumerate(files, 1):
        display_name = file.replace(shared_string, "").replace(extension, "")
        print(f"[{i}] {display_name}")

    choice = input("Enter the number of the char you want or write the name for a new char: ")
    try:
        choice_int = int(choice)
        if 1 <= choice_int <= len(files):
            selected_char = files[choice - 1].replace(shared_string, "").replace(extension, "")
            print(f"You selected: {selected_char}")
            return selected_char
        else:        
            print("Invalid input. Please enter a correct number.")
            return None
    except:
        print(f"You've created: {choice}")
        return choice

def prompter(role, content):
    message = '<|im_start|>'+ role +' \n' + content + '<|im_end|> \n'
    return message

def promp_generator(content):
    prompt = content +  '<|im_start|>assistant \n'
    return prompt

def history_update_print(role, conversation, conversation_dict, content, print_history=False, file_name=None):
    conversation += prompter(role, content)
    conversation_dict.append({"role": role, "content": content})
    if print_history:
        keys = conversation_dict[0].keys()
        history_path = os.path.join("history", f'history_{file_name}.csv')
        with open(history_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            writer.writerows(conversation_dict)
    return conversation, conversation_dict