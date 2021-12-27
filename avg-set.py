def average(arr):
    # your code goes here
    sett = set(arr)
    ans = sum(sett)/len(sett)
    avg = round(ans,3)
    return avg    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
