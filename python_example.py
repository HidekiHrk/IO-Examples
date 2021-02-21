import sys
import tty
tty.setraw(sys.stdin)
while True:
    char = sys.stdin.read(1)
    if char == '\x03':
        break
    sys.stdout.write(f'Tecla: {char}\n')
