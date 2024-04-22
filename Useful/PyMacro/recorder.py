import os
import keyboard

log_file = '/Users/maximilianmcclelland/github/RandomProjects/Useful/PyMacro/keystrokes.txt'

os.remove(log_file)

def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))
        print('{}\n'.format(event.name))

        if(event.name == "esc"):
            quit()

keyboard.on_press(on_key_press)

keyboard.wait()