#https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter

X = int(input())
shoe_sizes = input().split()
sizes = [int(size) for size in shoe_sizes]
N = int(input())

customers = []

for i in range(N):
  customer = [tuple(int(x) for x in input().split())]
  customers = customers + customer

earnings = 0

for size, price in customers:
  if size in sizes:
    sizes.remove(size)
    earnings += price
    
print(earnings)
