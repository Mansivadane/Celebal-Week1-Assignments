m = int(input())
set_a = set(map(int, input().split()))
n = int(input())
set_b = set(map(int, input().split()))
set_a_diff = set_a.difference(set_b)
set_b_diff = set_b.difference(set_a)
for i in sorted(set_a_diff.union(set_b_diff)):
    print(i)