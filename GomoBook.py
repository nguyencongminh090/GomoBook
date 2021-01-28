import os
from colorama import init, Fore, Style


init()
def main():
    f = open('DB.txt', 'r')
    db = f.read().split('\n')
    f.close()
    db = [i.split(' ') for i in db]
    while True:
        move = []
        inp = input('--> Input move: ')
        if inp == 'quit':
            break
        elif inp == 'clear':
            os.system('cls')
        inp = inp.split(' ')
        while '' in inp:
            inp.remove('')
        for i in db:
            try:
                if False not in [i[j] == inp[j] for j in range(len(inp))]:
                    if i[len(inp)] not in move:
                        move.append(i[len(inp)])
                        print('[+]', Fore.LIGHTRED_EX + str(i[len(inp)]) + Style.RESET_ALL, '| Len:', len(i))
                    else:
                        continue
            except:
                print('End')
                break

    pass


if __name__ == '__main__':
    main()
