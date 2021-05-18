n = None
lst = []
while n != 0:
    n = int(input())
    lst.append(n)
lst.sort()
m = max(lst)
print(lst.count(m))

a, b = int(input()), int(input())
while a != b:
    if (a // 2 >= b) and (a % 2 == 0):
        print(':2')
        a //= 2
    else:
        print('-1')
        a -= 1
