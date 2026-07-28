nums = [3,4,5,2]
max1 = 0
max2 = 0
for n in nums:
    if n > max1:
        max2 = max1
        max1 = n
    elif n > max2:
        max2 = n
print((max1-1)*(max2-1))