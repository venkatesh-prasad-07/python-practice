# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = map(int,input().split())
a = defaultdict(list)


i=0
for i in range(n):
    a[input()].append(str(i+1))

for j in range(m):
    print(' '.join(a[input()]) or -1)
    
    
