# -*- coding: utf-8 -*-
# 演算法分析機測
# 學號: 11020107 / 11020137 / 11020140
# 姓名: 蘇伯勳 / 關翔謙 / 葉柏榆
# 中原大學電機資訊學士班

import time
import heapq

class Edge:
    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight

def Dijkstra(src, dst, edges): # DP
    # init
    distance = {edge.dst: float('inf') for edge in edges} # init distances of src to all dst are positive infinite
    distance[src] = 0  # dtstance of src to itself is 0
    min_heap = [(0, src)] # init pq with src: (distance, node)
    # previous = {}  # To store previous node in the path

    while min_heap:
        cur_dist, cur_node = heapq.heappop(min_heap) # get min
        # if cost much, skip
        if cur_dist > distance[cur_node]:
            continue

        # update neighbors
        for edge in edges:
            if edge.src == cur_node:
                new_dist = cur_dist + edge.weight
                if new_dist < distance[edge.dst]:
                    distance[edge.dst] = new_dist
                    heapq.heappush(min_heap, (new_dist, edge.dst))
                    # previous[edge.dst] = cur_node  # Update previous node
    '''
    # output path
    path = [dst]
    while path[-1] != src:
        path.append(previous[path[-1]])
    path.reverse()
    '''

    # output
    print(f'{src} to {dst} = {distance[dst]}')

################### If using A-Star algorithm: #################################################################################

def euclidean_distance(src, dst):
    # Calculate Euclidean distance between two points
    return ((dst[0] - src[0]) ** 2 + (dst[1] - src[1]) ** 2) ** 0.5

def AStar(src, dst, edges):
    # Convert vertices to coordinates for Euclidean distance calculation
    vertices = {edge.src: (edge.src // 2, edge.src % 2) for edge in edges}
    vertices[dst] = (dst // 2, dst % 2)  # Add destination vertex
    
    # Initialize distances
    distance = {edge.dst: float('inf') for edge in edges}
    distance[src] = 0
    # previous = {}  # To store previous node in the path
    
    # Priority queue for A* algorithm
    open_set = [(0, src)]  # (f(n), node)
    
    while open_set:
        _, cur_node = heapq.heappop(open_set)
        
        if cur_node == dst:
            break  # Reached destination
        
        for edge in edges:
            if edge.src == cur_node:
                new_dist = distance[cur_node] + edge.weight
                if new_dist < distance[edge.dst]:
                    distance[edge.dst] = new_dist
                    # previous[edge.dst] = cur_node  # Update previous node
                    f_score = new_dist + euclidean_distance(vertices[edge.dst], vertices[dst])
                    heapq.heappush(open_set, (f_score, edge.dst))
    
    '''
    # output path
    path = [dst]
    while path[-1] != src:
        path.append(previous[path[-1]])
    path.reverse()
    '''
    
    # output
    print(f'{src} to {dst} = {distance[dst]}')
    
################################################################################################################################

def main():
    # read inputs
    vertices_sum = int(input())
    edges_sum = int(input())
    src_vertex = int(input()) # serial number of source vertex
    edges = []
    to_achieve = set()
    for _ in range(edges_sum):
        temp = list(map(int, input().split()))
        edges.append(Edge(temp[0], temp[1], temp[2]))
        if temp[0] != src_vertex:
            to_achieve.add(temp[0])
    to_achieve = sorted(to_achieve)
    input() # end
    print()

    # execute
    #start_time = time.time()

    for dst in to_achieve:
        Dijkstra(src_vertex, dst, edges)
    
    '''
    print()

    for dst in to_achieve:
        AStar(src_vertex, dst, edges)
    '''

    #total_time = time.time() - start_time
    #print(total_time)

# main()

''' Inputs
5
7
1
1 2 2
1 5 10
2 3 3
2 5 7
3 4 4
4 5 5
5 3 6
0
'''