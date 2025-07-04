# -*- coding: utf-8 -*-
# �t��k���R����
# �Ǹ�: 11020107 / 11020137 / 11020140
# �m�W: Ĭ�B�� / ������ / ���f��
# ����j�ǹq����T�Ǥh�Z

import time

def Actions(data):
    a = 0
    b = 0
    while b != data[2]:
        if a == 0:
            print('Fill A')
            a = data[0]
        elif b == data[1]:
            print('Empty B')
            b = 0
        else:
            print('Pour A B')
            temp = min(a, data[1] - b)
            a -= temp
            b += temp
    print('Success')
    return

def main():
    data = []
    while True:
        #print('Input (A\'s capacity, B\'s capacity, goal capacity(\"0 0 0\" means quit)): ', end = '')
        capacities = list(map(int, input().split()))
        if all(x == 0 for x in capacities):
            break
        data.append(capacities)
    
    for d in data:
        start_time = time.time()
        Actions(d)
        total_time = time.time() - start_time
        #print(f'Execution time: {total_time}')

if __name__ == '__main__':
    main()