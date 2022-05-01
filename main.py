from pathlib import Path
import time
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

cd = lambda _: os.chdir(_)

readFile = lambda _: open(_,"r").read()

#TODO: Add help/manpage
#TODO: Add feature to view contents of directory without cd
#TODO: Add feature to create/delete/move folders & files

def main():
    while True:
        os.system('cls')
        print_box(get_contents())
        options = '(cd) to change directory\t(open) to open file\t(help) to open manpage\t(exit) to exit\n'
        cmd = str(input(options))
        if any(map(lambda _: _ in cmd, ('cd','open'))): run_cmd, file = cmd.split(' ', 1)
        else: exit()
        if run_cmd == 'cd': cd(file)
        elif run_cmd == 'open':
            os.system('cls')
            print(readFile(file))
            input('<Enter to exit...>')
        else: exit()

if __name__ == '__main__':
    main()
