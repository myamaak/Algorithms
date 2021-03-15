# brute-force O(n^3)
def getSubsum(data) :

    max_value = -9999999999
    for i in range(len(data)-1):
        for j in range(i, len(data)):
            max_value = max(sum(data[i:j+1]), max_value)
        
    return max_value

#divide-and-conquer -> O(nlogn)
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

#dynamic programming -> O(n)

#f(i) = 인덱스 i를 오른쪽 끝으로 갖는 구간의 최대합
#f(i) = max(0, f(i-1))+arr[i]   (if i >0)
#     = arr[i]                  (if i==0)

def getSubsum(data) :

    dp = [i for i in data] 
    for i in range(1, len(data)): #f(0) = arr[0] 이므로 1부터 시작한다.
        dp[i] = max(dp[i-1] + data[i], data[i])
        #-> dp[i] = max(0, dp[i-1]) + data[i] 과 동일하다.
    
    return max(dp)

#바보풀이
# def getSubsum(data) :
#     dp =[]
#     n = len(data)
#     for i in range(n):
#         max_sum = 0
#         for j in range(i,n+1):
#             max_sum = max(max_sum, sum(data[i:j]))
#         dp.append(max_sum)
#     return max(dp)