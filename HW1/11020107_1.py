# -*- coding: utf-8 -*-
# 演算法分析機測
# 學號: 11020107 / 11020137 / 11020140
# 姓名: 蘇伯勳 / 關翔謙 / 葉柏榆
# 中原大學電機資訊學士班

import time

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def BuildTree(preorder, inorder):
  if not preorder or not inorder:
    return None
  
  root_val = preorder[0]
  root = TreeNode(root_val)
  root_index = inorder.index(root_val)

  root.left = BuildTree(preorder[1:1 + root_index], inorder[:root_index])
  root.right = BuildTree(preorder[1 + root_index:], inorder[root_index + 1:])

  return root

def GetPostorder(root):
  return "" if not root else GetPostorder(root.left) + GetPostorder(root.right) + str(root.val)

def main():
  results = []
  time_results = []

  while True:
    #prefix = input("頛詨?亙??摨????甇?: ")
    prefix = input()
    # 0 蝯????
    if (prefix == '0'):
      break
    #infix = input("頛詨?乩葉摨????甇?: ")
    infix = input()
    start_time = time.time()
    result = GetPostorder(BuildTree(prefix, infix))
    total_time = time.time() - start_time
    results.append(result)
    time_results.append(total_time)
    
  for result, time_result in zip(results, time_results):
    print(f"{result}")
    #print(f"??瑁????????: {time_result}\n")

if __name__ == "__main__":
  main()
