from itertools import product
A_str = input()
B_str = input()
A_str = A_str.split()
A_map = map(int,A_str)
A = tuple(A_map)
B_str = B_str.split()
B_map = map(int,B_str)
B = tuple(B_map)
result = list(product(A,B))
for i in result:
    print(i, end = " ");
