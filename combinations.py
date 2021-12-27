# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,r = input().split()

for i in range(1,int(r)+1):
    for j in combinations(sorted(s),i):
        print("".join(j))
