# -*- coding: utf-8 -*-
# 演算法分析機測
# 學號: 11020107 / 11020137 / 11020140
# 姓名: 蘇伯勳 / 關翔謙 / 葉柏榆
# 中原大學電機資訊學士班

if __name__ == '__main__':
    answers = [__import__('11020107_1'), __import__('11020107_2'), __import__('11020107_3'), __import__('11020107_4'), __import__('11020107_5')]
    while True:
        try:
            command = int(input('Input command(0 for quit, 1~5 for questions 1~5): '))
            if command == 0:
                break
            elif 1 <= command and command <= 5:
                answers[command-1].main()
            else:
                print('Invalid command, try again.')
        except Exception as e:
            print('Invalid command or illegal input, try again.')

'''
Inputs of prob. 1:
3 10 2 1 20
50 3 10 7 40 80
0

Inputs of prob. 2:
50
3
10 60
20 100
30 120
0

Inputs of prob. 3:
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

Inputs of prob. 4:
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

Inputs of prob. 5:
maze1.bmp
maze2.bmp
maze3.bmp
maze4.bmp
'''

''' Execution log
Input command(0 for quit, 1~5 for questions 1~5): 1
3 10 2 1 20
50 3 10 7 40 80
0

Length of LIS = 3
LIS = < 3, 10, 20 >

Length of LIS = 4
LIS = < 3, 7, 40, 80 >
Input command(0 for quit, 1~5 for questions 1~5): 2
50
3     
10 60 
20 100
30 120
0     

Total value = 220
Items = 2, 3
Input command(0 for quit, 1~5 for questions 1~5): 3
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

a = 0
b = 101
c = 100
d = 111
e = 1101
f = 1100
Decode = abcdef

A = 0100
B = 011
C = 11
D = 10
E = 00
F = 0101
Decode = BAD
Input command(0 for quit, 1~5 for questions 1~5): 4
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

1 to 2 = 2
1 to 3 = 5
1 to 4 = 9
1 to 5 = 9
Input command(0 for quit, 1~5 for questions 1~5): 5
Enter file name: maze1.bmp
Input command(0 for quit, 1~5 for questions 1~5): 5
Enter file name: maze2.bmp
Input command(0 for quit, 1~5 for questions 1~5): 5
Enter file name: maze3.bmp
Input command(0 for quit, 1~5 for questions 1~5): 5
Enter file name: maze4.bmp
Input command(0 for quit, 1~5 for questions 1~5): 0
'''