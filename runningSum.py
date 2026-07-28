nums = [1,2,3,4]
result = []
sum=0
for n in nums:
    result.append(sum+n)
    sum+=n
print(result)