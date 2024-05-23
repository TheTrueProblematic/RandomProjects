from tkinter import *
import time

# create root window
root = Tk()

# root window title and dimension
root.title("Auto MKV")
# Set geometry(widthxheight)
root.geometry('700x600')

def levelSetError():
    print("Level Set Error")

# function to set notification level
def setLevel(level):
    global status
    if status != 2:
        print(f"Notification level set to {level}")
        status = 5
        update_status()
    else:
        levelSetError()

# function to handle Start button click
def start():
    global status
    status = 2
    update_status()

# function to handle Stop button click
def stop():
    global status
    global launchTime
    status = 1
    update_status()
    print(time.time()-launchTime)

# function to update the status message
def update_status():
    global status
    messages = {
        1: "Ready",
        2: "Running...",
        3: "n/a",
        4: "Stopping...",
        5: "Notification Status Updated",
        6: "This is a longer message to make sure that a longer message can still fit."
    }
    status_label.config(text=messages.get(status, "Unknown status"))

def oneFile():
    print(one_file_mode.get())

# adding menu bar in root window
menu = Menu(root)

notifications_menu = Menu(menu, tearoff=0)
notifications_menu.add_command(label='Max', command=lambda: setLevel(3))
notifications_menu.add_command(label='Matt', command=lambda: setLevel(2))
notifications_menu.add_command(label='Both', command=lambda: setLevel(1))
menu.add_cascade(label='Notifications', menu=notifications_menu)

root.config(menu=menu)

# adding a large title to the root window
title = Label(root, text="Auto MKV", font=("Arial", 80), fg="#003366")
title.grid(column=0, row=0, columnspan=3, pady=30)

# creating a frame to hold the buttons
button_frame = Frame(root)
button_frame.grid(column=0, row=1, columnspan=3, pady=30)

# adding Stop and Start buttons to the frame
stop_btn = Button(button_frame, text="Stop", fg="red", bg="black", font=("Arial", 24), width=10, height=2, command=stop)
stop_btn.pack(side=LEFT, padx=20)

start_btn = Button(button_frame, text="Start", fg="green", bg="black", font=("Arial", 24), width=10, height=2, command=start)
start_btn.pack(side=RIGHT, padx=20)

# creating a frame for the switch
switch_frame = Frame(root)
switch_frame.grid(column=0, row=2, columnspan=3, pady=20)

# adding a Checkbutton for one file mode
one_file_mode = BooleanVar()
one_file_checkbutton = Checkbutton(switch_frame, text="One File Mode", variable=one_file_mode, font=("Arial", 24), padx=20, pady=10, command=oneFile)
one_file_checkbutton.pack()

# adding a status window below the buttons
status_frame = Frame(root, bd=2, relief="solid")
status_frame.grid(column=0, row=3, columnspan=3, padx=50, pady=30, sticky="ew")

status_label = Label(status_frame, text="", font=("Arial", 18), padx=10, pady=10)
status_label.pack(fill="both", expand=True)

# Set columns to be stretchable
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Set rows to be stretchable
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

# Initialize status variable
status = 1
launchTime = time.time()
update_status()

# Execute Tkinter
root.mainloop()
