# -*- coding: utf-8 -*-
# 演算法分析機測
# 學號: 11020107 / 11020137 / 11020140
# 姓名: 蘇伯勳 / 關翔謙 / 葉柏榆
# 中原大學電機資訊學士班

import time

def main():
    # read inputs
    data = []
    while (True):
        temp = list(map(int, input().split()))
        if len(temp) == 1 and 0 in temp:
            break
        data.append(temp)
    print()

    # execute
    #start_time = time.time()

    for i, cur_d in enumerate(data):
        l = len(cur_d)
        # LIS := an increasing sublist of cur_d, end up with cur_d[i]
        dp = [1] * l # store lis length at each i (iteration)
        prev = [-1] * l # store previous num's index
        for j in range(1, len(cur_d)):
            for k in range(j):
                if cur_d[k] <= cur_d[j] and dp[k] + 1 >= dp[j]:
                    dp[j] = dp[k] + 1
                    prev[j] = k
        
        # build LIS
        lis = []
        max_index = dp.index(max(dp))
        while max_index != -1:
            if cur_d[max_index] not in lis:
                lis.append(cur_d[max_index])
                max_index = prev[max_index]
            else:
                max_index = -1
        lis.reverse()

        # output
        print(f'Length of LIS = {len(lis)}')
        print(f'LIS = <', end = '')
        for j, num in enumerate(lis):
            print(f' {num}', end = '')
            if j != len(lis)-1:
                print(',', end = '')
        print(' >')

        if i != len(data)-1:
            print()

    #total_time = time.time() - start_time
    #print(total_time)

# main()

''' Inputs
3 10 2 1 20
50 3 10 7 40 80
0
'''

''' Explanation
cur_d = [3, 10, 2, 1, 20]
Length of LIS = 3
prev = [-1, 0, -1, -1, 1]
dp = [1, 2, 1, 1, 3]

=> LIS's length = max(dp) = 3 at index = 4
=> build LIS:
    index = 4: cur_d[4] = 20, prev[4] = 1 means previous num at index = 1, lis.append(20) -> lis = [20]
    index = 1: cur_d[1] = 10, prev[1] = 0 means previous num at index = 0, lis.append(10) -> lis = [20, 10]
    index = 0: cur_d[0] = 3, prev[0] = -1 means there is no previous num, lis.append(3) -> lis = [20, 10, 3]
    reverse -> lis = [3, 10, 20]

=> LIS = < 3, 10, 20 >

##########################################################

cur_d = [50, 3, 10, 7, 40, 80]
Length of LIS = 4
prev = [-1, -1, 1, 1, 3, 4]
dp = [1, 1, 2, 2, 3, 4]

=> LIS's length = max(dp) = 4 at index = 5
=> build LIS:
    index = 5: cur_d[5] = 80, prev[5] = 1 means previous num at index = 4, lis.append(80) -> lis = [80]
    index = 4: cur_d[4] = 40, prev[4] = 3 means previous num at index = 3, lis.append(40) -> lis = [80, 40]
    index = 3: cur_d[3] = 7, prev[3] = 1 means previous num at index = 1, lis.append(7) -> lis = [80, 40, 7]
    index = 1: cur_d[1] = 3, prev[1] = -1 means there is no previous num, lis.append(3) -> lis = [80, 40, 7, 3]
    reverse -> lis = [3, 7, 40, 80]

=> LIS = < 3, 7, 40, 80 >
'''