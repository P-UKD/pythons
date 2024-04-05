n = int(input())
m = int(input())

for x in range(-n, n, m):
    if x % 2 == 0:
        print(x)