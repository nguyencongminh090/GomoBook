from getdb import fplay
import os
import threading
from time import perf_counter as clock


from multiprocessing import Process


def als(data):
    return data.split(' ')


def chk(name='DB.txt'):
    a = clock()
    out = []
    f = open(name, 'r')
    lists = f.read().split('\n')
    f.close()
    for i in lists:
        out.append(als(i))
    b = clock()
##    print('Runtime: %.2f sec' % (b-a))
    return out


def main():
    a = os.popen('dir Database\\*.txt' + '/b')
    a = a.read()
    data = a.split('\n')
    s = 0
    fail = 0
    lst = []
    while '' in data:
        data.remove('')
    for i in data:
        try:
            f = open('DB.txt', 'a+')
            dbm = fplay('Database\\' + i)
            if dbm not in chk():
                dbr = ' '.join(dbm)
                f.write(dbr + '\n')
                f.close()
                s += 1
                lst.append('Database\\' + i)
            else:
                raise ValueError('Exist!')
        except:
            fail += 1
    
    print('Report')
    if len(lst) > 0:        
        print('----------\n**Success {} file:'.format(len(lst)))
        for i in lst:
            print('\t' + i)
        print('**Fail {} file:'.format(len(data) - len(lst)))
        for i in range(len(lst)):
            tmp = lst[i].split('Database\\')[1]
            lst.pop(i)
            lst.insert(i, tmp)
        for i in data:
            if i not in lst:
                print('\t' + i)
    else:
        print('**Fail to create book')
        for i in range(len(lst)):
            tmp = lst[i].split('Database\\')[1]
            lst.pop(i)
            lst.insert(i, tmp)
        for i in data:
            if i not in lst:
                print('\t-', i, '| Fail')
            else:
                print('\t-', i, '| Success')
    print('**Percent: {}%'.format(round((len(lst) / len(data)), 2)*100))
        


if __name__ == '__main__':
    main()
    os.system('pause>nul')
