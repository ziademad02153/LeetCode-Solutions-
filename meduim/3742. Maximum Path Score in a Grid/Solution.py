class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[-1] * (k + 1) for _ in range(n)]
        
        dp[0][0] = 0
        
        for r in range(m):
            row = grid[r]
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                
                val = row[c]
                cur = dp[c]
                limit = r + c
                if limit > k: limit = k
                
                if val == 0:
                    if c > 0:
                        left = dp[c-1]
                        if r > 0:
                            for j in range(limit + 1):
                                if left[j] > cur[j]:
                                    cur[j] = left[j]
                        else:
                            dp[c] = left[:]
                else:
                    if c > 0 and r > 0:
                        left = dp[c-1]
                        for j in range(limit, 0, -1):
                            t = cur[j-1]
                            l = left[j-1]
                            prev_best = t if t > l else l
                            if prev_best != -1:
                                cur[j] = prev_best + val
                            else:
                                cur[j] = -1
                        cur[0] = -1
                    elif c > 0:
                        left = dp[c-1]
                        for j in range(limit, 0, -1):
                            prev = left[j-1]
                            cur[j] = prev + val if prev != -1 else -1
                        cur[0] = -1
                    else:
                        for j in range(limit, 0, -1):
                            prev = cur[j-1]
                            cur[j] = prev + val if prev != -1 else -1
                        cur[0] = -1
                        
        ans = -1
        final_cell = dp[n-1]
        for score in final_cell:
            if score > ans:
                ans = score
        return ans