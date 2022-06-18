n = int(input())
arr = list(map(int, input().split()))
x = -9999
for i in range(0, n):
    if arr[i] < max(arr) and arr[i] > x:
        x = arr[i]
print(x)
