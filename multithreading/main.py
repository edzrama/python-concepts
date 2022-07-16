import threading
import time


class Painter:

    def __init__(self):
        self.paintwall()

    def paintwall(self):
        time.sleep(2)
        print('Wall has been painted')


# will wait for the process to complete before going the next one
Painter()
Painter()
Painter()
Painter()
print('\n')


class Painter_Threading:

    def __init__(self):
        t = threading.Thread(target=self.paint_it)
        t.start()

    def paint_it(self):
        time.sleep(2)
        print('\nDone Painting')

# will 'create' threads to run the call simultaneously
Painter_Threading()
Painter_Threading()
Painter_Threading()
Painter_Threading()
