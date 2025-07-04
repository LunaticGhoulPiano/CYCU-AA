# -*- coding: utf-8 -*-
# 演算法分析機測
# 學號: 11020107 / 11020137 / 11020140
# 姓名: 蘇伯勳 / 關翔謙 / 葉柏榆
# 中原大學電機資訊學士班

import os
import cv2
import time
import numpy as np
from collections import deque

def bfs(img, start, end): # get shortest path (only contains 1 pixel)
    rows, cols, _ = img.shape
    queue = deque([(start, [start])]) # (start coordinate, list of coordinates on the path start with start coordinate)
    visited = set()
    visited.add(start)
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == end: # reach end
            return path
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # up, down, left, right
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols # check current pixel in image
                and tuple(img[nx, ny]) == (0, 0, 0) # check boundaries is in black area
                and (nx, ny) not in visited): # check if already visited
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    
    return None

def getStartEnd(img): # find the appropriate starting / ending single pixel
    start = (0, 0)
    end = (len(img) - 1, len(img[0]) - 1) # (499, 499)

    return start, end

def bold_path(img, path, bold): # add surrounding 'bold' pixels of path(original shortest path only contains 1 pixel) into path
    pass

def main():
    # read input
    while True:
        ifs = input('Enter file name: ')
        if ifs.rfind('.') == -1:
            ifs += '.bmp'
        
        if os.path.exists(ifs):
            img = cv2.imread(ifs, -1)
            break
        else:
            print(f'File {ifs} doesn\'t exist !')

    # execute
    #start_time = time.time()

    # calculate start and end pixel
    start, end = getStartEnd(img)

    # BFS to find shortest path
    path = bfs(img, start, end)

    # mark with the color blue
    if path:
        bold = 4
        bold_path(img, path, bold) # bold path with surrounding 'bold' pixels

        # draw path with color blue
        for (x, y) in path:
            img[x, y] = [255, 0, 0] # blue is #0000FF i.e. rgb(0, 0, 255)

        # output
        dot_index = ifs.rfind('.')
        ofs = ifs[:dot_index] + 'sol.bmp'
        cv2.imwrite(ofs, img)
    else:
        print('Shortest path not found !')

    #total_time = time.time() - start_time
    #print(total_time)

# main()

''' Inputs
maze1.bmp
maze2.bmp
maze3.bmp
maze4.bmp
'''