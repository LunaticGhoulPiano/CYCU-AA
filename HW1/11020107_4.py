# -*- coding: utf-8 -*-
# �t��k���R����
# �Ǹ�: 11020107 / 11020137 / 11020140
# �m�W: Ĭ�B�� / ������ / ���f��
# ����j�ǹq����T�Ǥh�Z

import time

def connected_components(image):
  label = 0
  areas = {} # ??��?????�???��??
  index_map = {} # ??��?????�?籤�????????索�?? 以�??�????�?

  def union(x, y):
    if x != y:
      areas[x] += areas[y]
      # ??��?? 並�?????�????�?籤�??�? ??��??�?�??????��??
      for idx in index_map[y]:
        image[idx[0]][idx[1]] = x
      index_map[x].extend(index_map[y])
      # ??��?�被??��???????????
      del areas[y]
      del index_map[y]

  def get_label(i, j):
    neighbors = set() # ??��??�?籤�?��?��?????

    # ???歷以?????????8??��??
    if i > 0 and image[i - 1][j] != 0:  # �???��??�?
      neighbors.add(image[i - 1][j])
    if j > 0 and image[i][j - 1] != 0:  # 左�?��??�?
      neighbors.add(image[i][j - 1])
    if i > 0 and j > 0 and image[i - 1][j - 1] != 0:  # 左�????��??�?
      neighbors.add(image[i - 1][j - 1])
    if i > 0 and j < len(image[i]) - 1 and image[i - 1][j + 1] != 0:  # ??��????��??�?
      neighbors.add(image[i - 1][j + 1])

    # ??��?????0 ?????��?��??�?
    if not neighbors:
      nonlocal label
      label += 1
      areas[label] = 1
      index_map[label] = [(i, j)]
      return label
    
    # ??��?????�?�?
    else:
      min_neighbor = min(neighbors)

      # ?????��??�?�?�?
      areas[min_neighbor] += 1
      index_map[min_neighbor].append((i, j))
      # ??��??�????�?�? ???�??????��?�併??��??�?�?籤中
      if len(neighbors) > 1:
        for neighbor in neighbors:
          union(min_neighbor, neighbor)

      return min_neighbor
      
  # 1 pass?????? 就�????? 
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
    # 0 0 �????
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
    print("??????�????�?")
    for row in image:
      print(row)
    '''
    print(f"Image #{i}")
    print("Number of Connected Components =", result[0])
    
    for j, (label,area) in enumerate(result[1].items(), 1):
       print(f"Connected Component {j} Area = {area}")

    # print(f"??��????????: {time_result}")
    print("")
    
if __name__ == "__main__":
  main()