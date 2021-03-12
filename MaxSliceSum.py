# brute-force O(n^3)
def getSubsum(data) :

    max_value = -9999999999
    for i in range(len(data)-1):
        for j in range(i, len(data)):
            max_value = max(sum(data[i:j+1]), max_value)
        
    return max_value

#divide-and-conquer


#dynamic programming
def getSubsum(data) :

    dp = [i for i in data]
    for i in range(1, len(data)):
        dp[i] = max(dp[i-1] + data[i], data[i])
    
    return max(dp)