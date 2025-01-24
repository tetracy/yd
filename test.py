import sys
import termios

fd = sys.stdin.fileno()
old = termios.tcgetattr(fd)
new = termios.tcgetattr(fd)
new[3] = new[3] & ~termios.ICANON


# view(h,j,k,l), command(:q), search(/)

kbinput ='' 



def read_kbinput():
    key = sys.stdin.read(1)
    global kbinput
    kbinput += key
    return key

def handle_kbinput(key):
    if key == ":":
        print("\x1B[999;0H:",end="")
    print(key, end ="")


def main():
    termios.tcsetattr(fd, termios.TCSADRAIN, new)
    while True:
        key = read_kbinput()
        handle_kbinput(key)
    termios.tcsetattr(fd, termios.TCSADRAIN, old)

if __name__ == "__main__":
    main()
