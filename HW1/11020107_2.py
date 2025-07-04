# -*- coding: utf-8 -*-
# 演算法分析機測
# 學號: 11020107 / 11020137 / 11020140
# 姓名: 蘇伯勳 / 關翔謙 / 葉柏榆
# 中原大學電機資訊學士班

import time

def HamiltonianCircuit(nodeNum, data):
    # init input states
    states = [[0] * (nodeNum) for _ in range(nodeNum)] # nodeNum + 1: return to orogin
    for state in data: # "-1" cuz 1(begin node)'s index is 0
        states[state[0]-1][state[1]-1] = 1 # A->B
        states[state[1]-1][state[0]-1] = 1 # B->A
    # init output path
    HamiltonianPath = [1]

    def DFS(pos):
        if pos == nodeNum: # iterate all nodes
            # check if the last node is connected to the begin node
            if states[HamiltonianPath[-1]-1][HamiltonianPath[0]-1] == 1:
                return True
            else:
                return False
        for node in range(1, nodeNum+1): # add to path
            # if current node is connected with the previous node and current node not in path
            if states[HamiltonianPath[pos-1]-1][node-1] == 1 and node not in HamiltonianPath:
                HamiltonianPath.append(node)
                if DFS(pos+1):
                    return True
                # if current can't develop a Hamiltonian circuit, delete from path
                HamiltonianPath.pop()
        return False
    
    DFS(1) # start from 1
    HamiltonianPath.append(1)
    return ' '.join(map(str, HamiltonianPath))

def main():
    #print('Input (number of nodes, number of edges): ', end = '')
    nodeNum, edgeNum = map(int, input().split())
    #print('Start inputing:')
    data = [tuple(map(int, input().split())) for _ in range(edgeNum)]
    input()
    print()
    
    start_time = time.time()
    print(HamiltonianCircuit(nodeNum, data))
    total_time = time.time() - start_time
    #print(f'Execution time: {total_time}')

if __name__ == '__main__':
    main()