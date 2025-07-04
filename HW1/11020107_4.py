# -*- coding: utf-8 -*-
# ºtºâªk¤ÀªR¾÷´ú
# ¾Ç¸¹: 11020107 / 11020137 / 11020140
# ©m¦W: Ä¬§B¾± / Ãöµ¾Á¾ / ¸­¬f·®
# ¤¤­ì¤j¾Ç¹q¾÷¸ê°T¾Ç¤h¯Z

import time

def connected_components(image):
  label = 0
  areas = {} # ??²å?????çµ???¢ç??
  index_map = {} # ??²å?????æ¨?ç±¤ç????????ç´¢å?? ä»¥è??é¬????æ­?

  def union(x, y):
    if x != y:
      areas[x] += areas[y]
      # ??¯å?? ä¸¦æ?????ä¸????æ¨?ç±¤æ??äº? ??¿å??å¤?é¤??????¯å??
      for idx in index_map[y]:
        image[idx[0]][idx[1]] = x
      index_map[x].extend(index_map[y])
      # ??ªé?¤è¢«??¯å???????????
      del areas[y]
      del index_map[y]

  def get_label(i, j):
    neighbors = set() # ??°å??æ¨?ç±¤æ?¹ç?ºé?????

    # ???æ­·ä»¥?????????8??°å??
    if i > 0 and image[i - 1][j] != 0:  # ä¸???¹å??ç´?
      neighbors.add(image[i - 1][j])
    if j > 0 and image[i][j - 1] != 0:  # å·¦æ?¹å??ç´?
      neighbors.add(image[i][j - 1])
    if i > 0 and j > 0 and image[i - 1][j - 1] != 0:  # å·¦ä????¹å??ç´?
      neighbors.add(image[i - 1][j - 1])
    if i > 0 and j < len(image[i]) - 1 and image[i - 1][j + 1] != 0:  # ??³ä????¹å??ç´?
      neighbors.add(image[i - 1][j + 1])

    # ??¨å?????0 ?????ºæ?°æ??ç±?
    if not neighbors:
      nonlocal label
      label += 1
      areas[label] = 1
      index_map[label] = [(i, j)]
      return label
    
    # ??¨å?????æ¨?ç±?
    else:
      min_neighbor = min(neighbors)

      # ?????¥æ??å°?æ¨?ç±?
      areas[min_neighbor] += 1
      index_map[min_neighbor].append((i, j))
      # ??¥æ??ä¸????æ¨?ç±? ???å®??????¨é?¨ä½µ??°æ??å°?æ¨?ç±¤ä¸­
      if len(neighbors) > 1:
        for neighbor in neighbors:
          union(min_neighbor, neighbor)

      return min_neighbor
      
  # 1 pass?????? å°±ç????? 
  for i in range(len(image)):
    for j in range(len(image[i])):
      if image[i][j] == 1:
        image[i][j] = get_label(i, j)
  
  return len(areas), areas

def read_image_from_input():
  images = []
  results = []
  time_results = []

  while True:
    rows, cols = map(int, input().split(" "))
    # 0 0 çµ????
    if rows == 0 and cols == 0:
      break
    start_time = time.time()
    image = []
    for _ in range(rows):
      line = input().strip()
      row = list(map(int, line))
      image.append(row)
    groups, areas = connected_components(image)
    total_time = time.time() - start_time

    results.append((groups, areas))
    time_results.append(total_time)
    images.append(image)

  return images, results, time_results

def main():
  #print("input image:")
  images, results, time_results = read_image_from_input()
  print()

  for i, (image, result, time_result) in enumerate(zip(images, results, time_results), 1):
    '''    
    print("??????è³????ï¼?")
    for row in image:
      print(row)
    '''
    print(f"Image #{i}")
    print("Number of Connected Components =", result[0])
    
    for j, (label,area) in enumerate(result[1].items(), 1):
       print(f"Connected Component {j} Area = {area}")

    # print(f"??·è????????: {time_result}")
    print("")
    
if __name__ == "__main__":
  main()