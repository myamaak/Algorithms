# brute-force O(n^3)
def getSubsum(data) :

    max_value = -9999999999
    for i in range(len(data)-1):
        for j in range(i, len(data)):
            max_value = max(sum(data[i:j+1]), max_value)
        
    return max_value

#divide-and-conquer
def getSubsum(data) :

    n = len(data)
    
    if n == 1:
        return data[0]
    
    mid = n//2
    left = getSubsum(data[:mid])
    right = getSubsum(data[mid:])
    
    Sum = 0
    
    leftSum = 0
    rightSum = 0
    
    for i in range(mid-1, -1, -1): # mid-1에서부터 0까지 -1씩 
        Sum+= data[i]
        leftSum = max(Sum, leftSum)
    
    Sum = 0
    
    for i in range(mid, n):
        Sum += data[i]
        rightSum = max(Sum, rightSum)
    
    return max([left, right, leftSum+rightSum])

#dynamic programming
def getSubsum(data) :

    dp = [i for i in data]
    for i in range(1, len(data)):
        dp[i] = max(dp[i-1] + data[i], data[i])
    
    return max(dp)