nums=[-1,-2,3,-4,3,6,-2]
maxsub=nums[0]
cursum = 0
for n in nums:
             if cursum<0:
                 cursum=0
             cursum+=n
             maxsub = max(maxsub,cursum)
print(maxsub)   