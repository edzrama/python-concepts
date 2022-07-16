import threading
from threading import Event

event = Event()

def my_function():
    print("Waiting for event to trigger \n")
    event.wait()
    # this will not fire until event is set
    print("Event has been trigger, continue processing whatever it is your doing....")


t = threading.Thread(target=my_function)
t.start()

user_in = input("Do you want to trigger the event? (y/n)\n")
if user_in == "y":
    event.set()