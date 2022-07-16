import threading
import time

path = "text.txt"
text = ""


def read_file():
    global path, text
    while True:
        with open(path, "r") as f:
            text = f.read()
        time.sleep(3)


def print_text():
    for x in range(30):
        print(text)
        time.sleep(1)


td = threading.Thread(target=read_file, daemon=True)
t = threading.Thread(target=print_text)

td.start()
t.start()
