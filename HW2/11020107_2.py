# -*- coding: utf-8 -*-
# 演算法分析機測
# 學號: 11020107 / 11020137 / 11020140
# 姓名: 蘇伯勳 / 關翔謙 / 葉柏榆
# 中原大學電機資訊學士班

import time

def knapsack(mw, items): # DP
    n = len(items)
    table = [[0] * (mw + 1) for _ in range(n + 1)] # 2d array: (max weight + 1) * (item amount + 1) to store total values

    # build table in buttom-up
    for i in range(1, n + 1):
        for w in range(1, mw + 1):
            if items[i - 1]['weight'] > w: # current item's weight is bigger than limited max weight
                table[i][w] = table[i - 1][w] # directly use the previous total value
            else: # consider the bigger one
                table[i][w] = max(table[i - 1][w], items[i - 1]['price'] + table[i - 1][w - items[i - 1]['weight']])

    # find the items included in the knapsack by backtracking through the table
    w = mw
    results = []
    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:
            results.append(items[i - 1]['serial'])
            w -= items[i - 1]['weight']

    return table[n][mw], sorted(results)

def main():
    # read input
    mw = int(input()) # maximum weight
    amount = int(input()) # items amount
    items = []
    for serial_num, _ in enumerate(range(amount)):
        data = list(map(int, input().split()))
        item = {
            'serial': serial_num + 1,
            'weight': data[0],
            'price': data[1]
        }
        items.append(item)
    input()
    print()

    # execute
    #start_time = time.time()

    tv, results = knapsack(mw, items) # total values, grabbed items' serial_num (ascending)

    # output
    print(f'Total value = {tv}')
    print('Items =', end = '')
    for i, serial in enumerate(results):
        print(f' {serial}', end = '')
        if i != len(results) - 1:
            print(',', end = '')
    print()

    #total_time = time.time() - start_time
    #print(total_time)

# main()

''' Inputs
50
3
10 60
20 100
30 120
0
'''