import sys

n = int(sys.stdin.readline())
my_dict = {}

for i in range(n):
    a, b = sys.stdin.readline().split()
    my_dict[a] = b

for j in sorted(my_dict)[::-1]:
    if my_dict.get(j) == 'enter':
        print(j)