#!/usr/bin/python

from random import randint

def six_n(lot, rows):
    rows = rows if rows < 101 else 100
    tmp_rnd = []
    rnds = []
    
    for i in range(rows):
        for j in range(lot):
            if len(tmp_rnd) == 6: break
            
            n = randint(1, lot)
            if n not in tmp_rnd: tmp_rnd.append(n)
                
        rnds.append(tmp_rnd)
        tmp_rnd = []
        print('|  ' + str(i + 1), end=". ")
        print(rnds[i], end="\t |\n")

    # this one causes duplicates in randint weeeew
    # sd = [[randint(1,lot) for j in range(6)] for i in range(rows)] if rows < 100 else []
    # for i, list_num in zip([j for j in range(len(sd))], sd):
    #     print(i + 1, end=". ")
    #     print(list_num)

print()
print('---------------6/42---------------')
six_n(42, 7)
print('----------------------------------')
print()

print('---------------6/45---------------')
six_n(45, 7)
print('----------------------------------')
print()

print('---------------6/49---------------')
six_n(49, 7)
print('----------------------------------')
print()

print('---------------6/55---------------')
six_n(55, 7)
print('----------------------------------')
print('''
  ____   _    _   _ _____ _   _ _____ ____  
 |  _ \ / \  | \ | |_   _| | | |_   _/ ___| 
 | |_) / _ \ |  \| | | | | | | | | | \___ \ 
 |  __/ ___ \| |\  | | | | |_| | | |  ___) | :)
 |_| /_/   \_\_| \_| |_|  \___/  |_| |____/ 
                                            
''')
