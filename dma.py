import sys
import tty
import termios
from threading import Thread
from time import sleep

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

pause = False
memory = []

def cpu_callback(result):
    global pause
    pause = True
    print('Processing input...', end="\r\n")
    input_result = ''.join(result)
    sleep(3)
    pause = False
    print("Resultado:", input_result, end="\r\n")

def dma(callback):
    tty.setraw(fd)
    print('-- DMA Initialized --', end="\r\n")
    for _ in range(5):
        char = sys.stdin.read(1)
        memory.append(char)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    callback(memory)

def process(number):
    while True:
        while pause:
            pass
        print(f'Process {number}', end="\r\n")
        sleep(number)

thread1 = Thread(target=process, args=(1,))
thread2 = Thread(target=process, args=(2,))
dma_thread = Thread(target=dma, args=(cpu_callback,))
thread1.start()
thread2.start()
sleep(5)
dma_thread.start()