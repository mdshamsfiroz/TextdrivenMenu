//The code defines several functions to perform different actions, such as opening the calendar, Chrome, File Explorer, Notepad, Command Prompt, Control Panel, Task Manager, and System Settings.
import os

print("Hey, I am your assistant.")

def open_calendar():
    print("Opening calendar...")
    os.system("start outlookcal:")

def open_chrome():
    print("Opening Chrome...")
    os.system("start chrome")

def open_file_explorer():
    print("Opening File Explorer...")
    os.system("start explorer")
    
def open_notepad():
    print("Opening Notepad...")
    os.system("start notepad")

def open_command_prompt():
    print("Opening Command Prompt...")
    os.system("start cmd")

def open_control_panel():
    print("Opening Control Panel...")
    os.system("start control")
    
def open_task_manager():
    print("Opening Task Manager...")
    os.system("start taskmgr")

def open_system_settings():
    print("Opening System Settings...")
    os.system("start ms-settings:")


def assistance():
    ch = input("How can I help you: ").strip()
    return ch


while True:
    ch = assistance()

    if ("run" in ch or "execute" in ch) and "cal" in ch:
        open_calendar()
    elif ("run" in ch or "open" in ch or "execute" in ch) and "chrome" in ch:
        if "don't" not in ch and "not" not in ch and "do not" not in ch:
            open_chrome()
        else:
            print("Okay, I won't open Chrome.")
    
    elif ("run" in ch or "execute" in ch) and "file explorer" in ch:
        open_file_explorer()
    elif ("run" in ch or "open" in ch) and "file explorer" in ch:
        if "don't" not in ch and "not" not in ch and "do not" not in ch:
            open_file_explorer()
        else:
            print("Okay, I won't open explorer.")
    
    elif ("run" in ch or "execute" in ch) and "notepad" in ch:
        open_notepad()
    elif ("run" in ch or "open" in ch) and "notepad" in ch:
        if "don't" not in ch and "not" not in ch and "do not" not in ch:
            open_notepad()
        else:
            print("Okay, I won't open notepad.")
            
    
    elif ("run" in ch or "execute" in ch) and ("cmd" in ch or "command prompt" in ch) :
        open_command_prompt()
    elif ("run" in ch or "open" in ch) and "cmd" in ch:
        if "don't" not in ch and "not" not in ch and "do not" not in ch:
            open_command_prompt()
        else:
            print("Okay, I won't open command prompt.")
    
    elif ("run" in ch or "execute" in ch) and "control panel" in ch :
        open_control_panel()
    elif ("run" in ch or "open" in ch) and "control panel" in ch:
        if "don't" not in ch and "not" not in ch and "do not" not in ch:
            open_control_panel()
        else:
            print("Okay, I won't open controlpanel.")
            
    elif ("run" in ch or "execute" in ch) and "task manager" in ch :
        open_task_manager()
    elif ("run" in ch or "open" in ch) and "task manager" in ch:
        if "don't" not in ch and "not" not in ch and "do not" not in ch:
            open_task_manager()
        else:
            print("Okay, I won't open task manager.")
    
    
    elif ("run" in ch or "execute" in ch) and "setting" in ch :
        open_system_settings()
    elif ("run" in ch or "open" in ch) and "setting" in ch:
        if "don't" not in ch and "not" not in ch and "do not" not in ch:
            open_system_settings()
        else:
            print("Okay, I won't open  system setting.")
    
            
    elif ch:
        print("Please type valid text....")
    else:
        print("Thank you, bye.")
        break
