from youdao import Youdao
import os
import sys
import subprocess

HIST_PATH = os.path.expanduser('~/Atext/yd/history.txt')

def txt_effect(s, effect=0):
    # ref: https://en.wikipedia.org/wiki/ANSI_escape_code
    return "\x1b[{}m{}\x1b[m".format(str(effect),s)

def add_history(word):
    hist = open(HIST_PATH,'r').read()
    if word not in hist:
        with open(HIST_PATH, 'a',encoding='utf-8') as f:
            f.write(word + "\n")

def main():
    if len(sys.argv) > 1:
        try:
            wd = Youdao(sys.argv[1])
            ec = wd.get_ec()
            os.system('clear')
            print(txt_effect(sys.argv[1],1))
            for i in ec:
                print(i)
            add_history(sys.argv[1])
        except:
            print('error')
    else:
        pass

if __name__ == '__main__':
    main()
