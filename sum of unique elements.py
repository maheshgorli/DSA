from collections import Counter


nums = [1,2,3,2]
count =Counter(nums)
sum=0
for n , values in count.items():
    if values == 1:
        sum += n
print(sum)