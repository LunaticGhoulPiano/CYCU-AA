# -*- coding: utf-8 -*-
# 演算法分析機測
# 學號: 11020107 / 11020137 / 11020140
# 姓名: 蘇伯勳 / 關翔謙 / 葉柏榆
# 中原大學電機資訊學士班

import time

class AStar:
    def __init__(self, h, neighbors):
        self.is_goal = lambda p: p == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
        self.h = h
        self.neighbors = neighbors
        self.found = object()

    def solve(self, init):
        self.path = [init]
        self.close_list = {init}
        self.path_des = []
        h = self.h(init)

        while True:
            t = self.search(0, h)
            if t is self.found: return self.path_des
            if t is None: return None
            h = t

    def search(self, g, h): # g: cost from starting node to current node, self.h(node): cost from current node to target node, f: their sum

        node = self.path[-1] # each node is a possible state(path)
        f = g + self.h(node) # LaTeX: {\displaystyle f(n)=g(n)+h(n)}
        if f > h: return f
        if self.is_goal(node): return self.found

        m = None # minimal cost
        for cost, n, des in self.neighbors(node): # cost to neighbors, neighbor nodes, directions(moves) to neighbors
            if n in self.close_list: continue

            self.path.append(n)
            self.close_list.add(n)
            self.path_des.append(des)
            t = self.search(g + cost, h) # update cost (for every move, cost == 1)

            if t == self.found: return self.found
            if m is None or (t is not None and t < m): m = t


            # return to top
            self.path.pop()
            self.path_des.pop()
            self.close_list.remove(n)

        return m

def slide_neighbors():
    movelist = []
    for gap in range(16):
        x, y = gap % 4, gap // 4 # set coordinates
        moves = [] # opposite possible moves, ex. gap = 4 -> coordinate = (0, 1) -> moves = [1(L), -4(D), 4(U)]
        if x > 0: moves.append(-1) # R
        if x < 3: moves.append(+1) # L
        if y > 0: moves.append(-4) # D
        if y < 3: moves.append(+4) # U
        movelist.append(moves) # horizontal moves: +-1, vertical moves: +-4

    def neighbors(p):
        gap = p.index(0) # index of '0'
        l = list(p) # current puzzle state

        for m in movelist[gap]: # generate states correspond to moves, movelist[gap]: possible moves of 0's corrdinate
            l[gap] = l[gap + m]
            l[gap + m] = 0
            yield (1, tuple(l), (l[gap], m)) # return ccorrespond state every single iterator call
            l[gap + m] = l[gap]
            l[gap] = 0

    return neighbors # return function neighbors

def slide_wd():
    wd_goal = [[0] * i + [4] + [0] * (3 - i) for i in range(4)]
    wd_goal[-1][-1] = 3
    wd_goal = tuple(sum(wd_goal, []))

    wd = {}
    to_visit = [(wd_goal, 0, 3)]
    while to_visit:
        cfg, cost, e = to_visit.pop(0)
        
        # encode cfg (hashing) for EVERY POSSIBLE STATE and add to to_visit to accelerate the efficiency of search
        enccfg = 0
        for i in range(len(cfg)):
            enccfg |= cfg[i] << (i*3)
        
        if enccfg in wd: continue
        wd[enccfg] = cost

        for d in [-1, 1]:
            if 0 <= e + d < 4:
                for c in range(4):
                    if cfg[4*(e+d) + c] > 0:
                        ncfg = list(cfg)
                        ncfg[4*(e+d) + c] -= 1
                        ncfg[4*e + c] += 1
                        to_visit.append((tuple(ncfg), cost + 1, e+d))

    goal = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
    goals = {i : goal.index(i) for i in goal}

    def h(p): # calculate Manhattan distance
        ht = 0 # Walking distance between rows.
        vt = 0 # Walking distance between columns.
        d = 0
        for i, c in enumerate(p):
            if c == 0: continue
            g = goals[c]
            xi, yi = i % 4, i // 4
            xg, yg = g % 4, g // 4
            ht += 1 << (((yi*4)+yg)*3)
            vt += 1 << (((xi*4)+xg)*3)

            if yg == yi:
                for k in range(i + 1, i - i%4 + 4): # Until end of row.
                    if p[k] and goals[p[k]] // 4 == yi and goals[p[k]] < g:
                        d += 2

            if xg == xi:
                for k in range(i + 4, 16, 4): # Until end of column.
                    if p[k] and goals[p[k]] % 4 == xi and goals[p[k]] < g:
                        d += 2

        d += wd[ht] + wd[vt] # LaTeX: {\displaystyle d(x,y)=\left|x_{1}-x_{2}\right|+\left|y_{1}-y_{2}\right|.}

        return d
    return h

def main():
    neighbors = slide_neighbors()
    slide_solver = AStar(slide_wd(), neighbors)

    # input
    tests = []
    num = int(input())
    for i in range(num):
        arr = []
        for j in range(4):
            tmp = input().split()
            tmp = [eval(j) for j in tmp]
            arr = [*arr, *tmp]
            
        tests.append(tuple(arr))
        if i != num - 1:
            input()

    # output
    for i, p in enumerate(tests, 1):
        start_time = time.time()
        moves = slide_solver.solve(p)
        total_time = time.time() - start_time
        print()
        print(f"Puzzle {i}:")
        print(f"Number of moves: {len(moves)}")
        print("Moves:")
        for j, move in enumerate(moves, 1):
            moved_number = move[0]
            move_direction = { -1: "R", 1: "L", -4: "D", 4: "U"}[move[1]]
            print(f"{moved_number:2}{move_direction}", end=" ")
            if j % 5 == 0:
                print()
            
        if len(moves) % 5 != 0:
            print()
        
        print(f'Executione time: {total_time}')
            
if __name__ == '__main__':
    main()