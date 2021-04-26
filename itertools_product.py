--https://www.hackerrank.com/challenges/itertools-product/problem
from itertools import product


a = (input())
a_list = (list((a).split()))
b = (input())
b_list = (list((b).split()))
int_a = [int(i) for i in a_list]
int_b = [int(i) for i in b_list]
cart_product_list = list(product(int_a, int_b))

cart_product = " ".join([str(i) for i in cart_product_list])
print(cart_product)
