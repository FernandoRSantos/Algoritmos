l = []
for x in range(10):
    n = int(input(f"Digite o {x}°: "))
    l.append(n)

t = tuple(l)
print(t[::-1])