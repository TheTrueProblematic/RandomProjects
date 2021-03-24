from serial import Serial
from dearpygui import core, simple
ser = Serial('com6')
t = True

with simple.window("Current Temp"):
    core.add_label_text("temp", "Hello world", color=[255, 255, 255])

core.start_dearpygui()

while t:
    read = str(ser.readline())
    l = len(read)
    end = l - 5
    subread = read[2:end]
    core.set_value("temp", subread)



