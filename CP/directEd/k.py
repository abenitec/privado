import random

l = []
for i in range(2):
    x = random.randint(1, 30)
    l.append(x)

l.extend([90])
print(dir(l))

x 

srtd = sorted(l)
print(srtd)
