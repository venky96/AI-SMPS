import math
import random

dist = input()
number_of_cities = int(input())
coordinates = dict()

for i in range(number_of_cities):
  coord_string_list = input().split()
  coordinates[f'{i}'] = (float(coord_string_list[0]), float(coord_string_list[1]))

dist_matrix = []

for i in range(number_of_cities):
  dist_list = [float(j) for j in input().split()]
  dist_matrix.append(dist_list)

def exp_decay(x):
  return int(2000*math.exp(-x/250))

def pathLength(path):
  length = 0
  path_list_size = len(path)
  for i in range(path_list_size):
    length += dist_matrix[path[i]][path[(i+1) % path_list_size]]
  return length 

def rev(path, i, j):
  return path[0:i] + list(reversed(path[i:j])) + path[j:]

def do2opt(path, i, j):
  return rev(path, i+1, j+1)

prev_path_length = 10000000000000
min_path = []
x=0

path = [i for i in range(number_of_cities)]
n = len(path)
for z in range(exp_decay(number_of_cities)):
    random.Random(z).shuffle(path)
    current_path_length = pathLength(path)
    found_improvement = True
    while found_improvement:
        found_improvement = False
        for i in range(0,n-1):
            for j in range(i+1, n):
                lengthDelta = 0 
                lengthDelta =  dist_matrix[path[i]][path[j]] + dist_matrix[path[(i+1) % n]][path[(j+1) % n]] - dist_matrix[path[i]][path[(i+1) % n]] - dist_matrix[path[j]][path[(j+1) % n]] 
                if lengthDelta < -0.1:
                    path = do2opt(path, i , j)
                    current_path_length += lengthDelta
                    found_improvement = True

    current_path_length = pathLength(path)
    if current_path_length < prev_path_length:
        print(current_path_length)
        min_path = path
        prev_path_length = current_path_length
        x+= 1
        print(' '.join([str(elem) for elem in min_path]))
