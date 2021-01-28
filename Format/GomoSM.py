from getdb import fplay
import os
import threading


def main():
    a = os.popen('dir Database\\*.txt' + '/b')
    a = a.read()
    data = a.split('\n')
    while '' in data:
        data.remove('')
    for i in data:
        status = 'Success'
        try:
            f = open('DB.txt', 'a+')
            dbr = ' '.join(fplay('Database\\' + i))
            f.write(dbr + '\n')
        except:
            status = 'Error'
        print('Name:', i, '| Status:', status)
        f.close()


if __name__ == '__main__':
    main()
