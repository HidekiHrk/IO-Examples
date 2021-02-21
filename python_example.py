import sys
import tty
tty.setraw(sys.stdin)
"""
Ao final da execução deste código, o seu terminal estará em modo raw
portanto, recomendo fechar e abrir novamente o seu emulador de terminal.
"""

while True:
    char = sys.stdin.read(1)
    if char == '\x03':
        break
    sys.stdout.write(f'Tecla: {char}\r\n')
