--https://www.hackerrank.com/challenges/itertools-product/problem
from itertools import product


a = (input())
a_list = (list((a).split()))
b = (input())
b_list = (list((b).split()))
int_a = [int(i) for i in a_list]
int_b = [int(i) for i in b_list]
x = list(product(int_a, int_b))

b = " ".join([str(i) for i in x])
print(b)
