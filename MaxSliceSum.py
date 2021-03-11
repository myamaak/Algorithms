# brute-force O(n^3)
def getSubsum(data) :

    max_value = -9999999999
    for i in range(len(data)-1):
        for j in range(i, len(data)):
            max_value = max(sum(data[i:j+1]), max_value)
        
    return max_value

#divide-and-conquer
