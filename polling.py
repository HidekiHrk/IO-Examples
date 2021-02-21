from threading import Thread
from time import sleep

pause = False

def process(number):
    while True:
        while pause:
            pass
        print(f'Process {number}')
        sleep(number)

thread1 = Thread(target=process, args=(1,))
thread2 = Thread(target=process, args=(2,))
thread1.start()
thread2.start()

sleep(5)
pause = True
print('Waiting for input:')
user_input = input('> ')
print(f'Input is: {user_input}')
pause = False
