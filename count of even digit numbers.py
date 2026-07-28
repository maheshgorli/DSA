nums = [12,345,2,6,7896]
count = 0
for n in nums:
    digits = 0
    temp=n
    while temp!=0:
        digits+=1
        temp//=10
    if digits%2==0:
        count+=1
print(count)
