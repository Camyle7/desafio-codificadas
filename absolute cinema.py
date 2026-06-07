import sys 
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list (map(int, input().split()))
    b = list (map(int, input().split()))

    S_total = sum(a) + sum(b)
    mins = [min(a[i], b[i]) for i in range(n)]
    sum_mins = sum(mins)
    best = max(mins)

    print(S_total - sum_mins + best)

t = int(input())
for _ in range(t):
    solve()
     
