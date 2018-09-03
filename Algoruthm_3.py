from time import *
t0 = time()
count = 10**5
nums = []
for i in range(count):
    nums.append(i)

nums.reverse()
t1 = time() - t0
print(t1)

r0 = time()
nums = []
for i in range(count):
    nums.insert(0,i)

t2 = time() - t0
print(t2)

