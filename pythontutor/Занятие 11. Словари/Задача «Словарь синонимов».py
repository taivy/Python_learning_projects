n = int(input())
d = {}
for i in range(n):
    k, v = input().split()
    d[k] = v
inv_d = {v:k for k,v in d.items()}
w = input()
if w in d:
    print(d[w])
else:
    print(inv_d[w])