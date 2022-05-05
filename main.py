from cProfile import run
from pathlib import Path
import shutil
import os

def get_contents():
    contents = f"\n{Path.cwd()}:\n"
    contents += f"{'-' * len(str(Path.cwd()))}\n"
    for x in Path('.').iterdir():
        contents += ('+  %s\n' %x) if x.is_dir() else ('*  %s\n' %x)
            #for xx in Path(x).iterdir():
            #    if xx.is_dir(): contents += ('   +  %s\n' %str(xx).lstrip(str(x)).lstrip("\\"))
            #    else: contents += ('   *  %s\n' %str(xx).lstrip(str(x)).lstrip("\\"))
    return str(contents)

def print_box(txt, indent=2):
    lines = txt.split('\n')
    width = max(map(len, lines))
    space = " " * indent
    box = f'+{"-"*(width + indent * 2)}+\n'
    box += ''.join([f'|{space}{line:<{width}}{space}|\n' for line in lines])
    box += f'+{"-" * (width + indent * 2)}+'
    print(box)

'''
Functions
'''
cd = lambda _: os.chdir(_)

readFile = lambda _: open(_,"r").read()

def removeFile(file):
    if file.is_dir(): shutil.rmtree(file)
    else: file.unlink()

def print_msg(msg):
    os.system('cls')
    print(msg)
    input('<Enter to exit...>') 

#TODO: Add feature to view contents of directory without cd
#TODO: Add feature to create/move folders & files

def main():
    while True:
        os.system('cls')
        print_box(get_contents())
        options = 'Main cmd: (cd) / (open) / (rm) / (help) / (exit)\n'
        cmd = str(input(options))
        if any(map(lambda _: _ in cmd, ('cd','rm','open','help'))):
            try:
                run_cmd, file = cmd.split(' ', 1)
            except ValueError:
                run_cmd = cmd
        else: exit()
        if run_cmd == 'cd': cd(file)
        elif run_cmd == 'rm': removeFile(Path(file))
        elif run_cmd == 'help':
            print_msg(HELP)
        elif run_cmd == 'open':
            print_msg(readFile(file))
        else: exit()

if __name__ == '__main__':
    main()