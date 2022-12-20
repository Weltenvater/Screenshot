from PIL import ImageGrab
import os
import time
from tkinter import messagebox

def screenGrab():
    print('noch 5 Secunden Zeit!')
    time.sleep(5)
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\Screenshot__' + str(int(time.time())) + 
'.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()
