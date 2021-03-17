def solution(land):
    answer = 0
    N = len(land)
    dp = [[None]*4 for i in range(N+1)]
    dp[0] = [0,0,0,0]

    for row in range(1,N+1):
        for i in range(4):
            dp[row][i] = max([dp[row-1][index] for index in range(4) if index !=i]) +land[row-1][i]

    return max(dp[N])