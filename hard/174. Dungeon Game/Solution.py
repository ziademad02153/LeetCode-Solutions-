class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        
        # Use a large integer instead of float('inf') for faster processing
        dp = [1 << 31] * (n + 1)
        dp[n - 1] = 1
        
        for i in range(m - 1, -1, -1):
            row = dungeon[i]
            for j in range(n - 1, -1, -1):
                # Inline comparison is faster than calling min()
                min_h = dp[j] if dp[j] < dp[j + 1] else dp[j + 1]
                
                req = min_h - row[j]
                dp[j] = req if req > 0 else 1
                
        return dp[0]