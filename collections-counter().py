# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
items = int(input())
sizes = Counter(map(int,input().split()))
no = int(input())
earnings=0
for i in range(no):
    s,c = map(int,input().split())
    if s in sizes and sizes[s]>0:
        sizes[s] = sizes[s]-1
        earnings +=c
        
print(earnings)        
