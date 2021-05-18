n = None
lst = []
while n != 0:
    n = int(input())
    lst.append(n)
lst.sort()
m = max(lst)
print(lst.count(m))
