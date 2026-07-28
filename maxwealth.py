accounts = [[1,2,3],[3,2,1]]
maxwealth=0
for a in accounts:
    wealth=sum(a)
    if wealth > maxwealth:
        maxwealth=wealth
print(maxwealth) 