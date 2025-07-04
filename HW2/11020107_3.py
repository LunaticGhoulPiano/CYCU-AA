# -*- coding: utf-8 -*-
# 演算法分析機測
# 學號: 11020107 / 11020137 / 11020140
# 姓名: 蘇伯勳 / 關翔謙 / 葉柏榆
# 中原大學電機資訊學士班

import time

class Node:
    def __init__(self, ch, f):
        self.ch = ch # character
        self.f = f # ferquency
        self.parent = None
        self.left = None
        self.right = None
        self.huffman_code = ''

def Encoder(nodes):
    while len(nodes) > 1:
        # sort by frequency(ascending) -> ASCII of character(ascending)
        nodes = sorted(nodes, key = lambda node: (node.f, ord(node.ch) if node.ch else float('inf')))

        # get left and right childs
        left = nodes.pop(0)
        right = nodes.pop(0)

        # set parent
        parent = Node(None, left.f + right.f)
        parent.left = left
        parent.right = right
        left.parent = parent
        right.parent = parent

        # append parent into nodes
        nodes.append(parent)
    
    def setHuffmanCode(node, code):
        if node is not None:
            node.huffman_code = code
            setHuffmanCode(node.left, code + '0')
            setHuffmanCode(node.right, code + '1')

    # encode
    setHuffmanCode(nodes[0], '')

    return nodes[0]

def Decoder(root, to_decode):
    cur_node = root
    decoded = ''

    for bit in to_decode:
        if bit == '0':
            cur_node = cur_node.left
        else:
            cur_node = cur_node.right
        
        # achieve leaf
        if cur_node.left is None and cur_node.right is None:
            decoded += cur_node.ch
            cur_node = root
    
    return decoded

def getLeaves(node):
    leaves = []
    if node is not None:
        if node.left is None and node.right is None:
            leaves.append(node)
        else:
            leaves.extend(getLeaves(node.left))
            leaves.extend(getLeaves(node.right))
    return leaves

def main():
    # read inputs
    data = []
    while True:
        n = int(input())
        if n == 0:
            break
        cur_d = []
        for _ in range(n):
            temp = tuple(map(str, input().split()))
            cur_d.append(Node(temp[0], int(temp[1]))) # char, frequency
        to_decode = str(input())
        data.append({'data': cur_d, 'to_decode': to_decode})
    print()

    # exectute
    #start_time = time.time()

    for i, cur_d in enumerate(data):
        # build tree
        root = Encoder(cur_d['data'])
        # get sorted leaves
        leaves = getLeaves(root)
        leaves = sorted(leaves, key = lambda node: ord(node.ch))
        # decode string
        decoded_str = Decoder(root, cur_d['to_decode'])
        # output
        for leaf in leaves:
            print(f'{leaf.ch} = {leaf.huffman_code}')
        print(f'Decode = {decoded_str}')
        
        if i != len(data)-1:
            print()
    
    #total_time - time.time() - start_time
    #print(total_time)

# main()

''' Inputs
6
a 45
b 13
c 12
d 16
e 9
f 5
010110011111011100
6
A 2
B 6
C 15
D 12
E 8
F 3
011010010
0
'''