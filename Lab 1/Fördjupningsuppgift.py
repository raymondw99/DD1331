#!/usr/bin/python
def ramanujan(n):
    List = []
    for a in range(1,(round(n**3) +1)):
        try:
            b = (n - a**3)**(1/3)
            num = (a**3 + (round(b)**3))
            if n == num:
                if a <= b:
                    List.append((a,round(b)))
        except TypeError:
            break
    return List

print(ramanujan(443889))
print(ramanujan(152))
print(ramanujan(3697))


