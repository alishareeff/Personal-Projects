import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data): #this function creates json file
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath): #reads the json file for us
    try:
        with open(filepath, "r") as f:
            data = json.load(f) #loading in this file
            return data
    except:
        return {}

if len(sys.argv) == 2: #we only want to accept one command after multiclipboard.py (that's why we check if there's 2)
    command = sys.argv[1] #we are accepting the 2nd argument (2nd element in list)
    data = load_data(SAVED_DATA)

    if command == "save":  #save command takes what's currently on clipboard and save it as a key in our json file
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("data saved!")

    elif command == "load":  #use this when you want to copy something to the clipboard
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard")
        else:
            print("key does not exist")

    elif command == "list":  #just outputs the all the data
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command")
