def getMaximumValue(weights, values, n, maxWeight):
    dp = [[-1 for _ in range(maxWeight + 1)] for _ in range(n)]
    def helper(i, w):
        # base case
        if i == 0:
            if weights[0] <= w:
                return values[0]
            else:
                return 0
        if dp[i][w] != -1:
            return dp[i][w]

        skip = helper(i - 1, w)
        pick = float('-inf')

        if weights[i] <= w:
            pick = values[i] + helper(i - 1, w - weights[i])

        dp[i][w] = max(skip, pick)
        return dp[i][w]

    return helper(n - 1, maxWeight)
