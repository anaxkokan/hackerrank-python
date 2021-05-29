#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
from collections import defaultdict

x, y = input().split(' ')
m, n = int(x), int(y)

A = []
B = []

for i in range(m):
  group_A = input()
  A.append(group_A)

for j in range(n):
  group_B = input()
  B.append(group_B)
 
letter_indices = defaultdict(list)

for i in range(m):
    letter_indices[A[i]].append(i+1)

for b in B:
    
  if b in letter_indices:
    str_b = map(str, letter_indices[b])
    print(" ".join(str_b))
  else:
    print(-1)

