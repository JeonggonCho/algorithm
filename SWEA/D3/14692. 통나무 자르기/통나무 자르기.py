T = int(input())

for i in range(1, T+1):
    N = int(input())
    if N % 2 == 0:
        print(f'#{i} Alice')
    else:
        print(f'#{i} Bob')