class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7

        # dp[i][j] = maximum score till (i, j)
        # cnt[i][j] = number of ways to get that maximum score
        dp = [[-1] * n for _ in range(n)]
        cnt = [[0] * n for _ in range(n)]

        dp[0][0] = 0
        cnt[0][0] = 1

        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                if i == 0 and j == 0:
                    continue

                mx = -1
                ways = 0

                for x, y in ((i - 1, j), (i, j - 1), (i - 1, j - 1)):
                    if x < 0 or y < 0:
                        continue
                    if dp[x][y] == -1:
                        continue

                    if dp[x][y] > mx:
                        mx = dp[x][y]
                        ways = cnt[x][y]
                    elif dp[x][y] == mx:
                        ways = (ways + cnt[x][y]) % MOD

                if mx == -1:
                    continue

                val = 0
                if board[i][j] != 'S':
                    val = int(board[i][j])

                dp[i][j] = mx + val
                cnt[i][j] = ways % MOD

        if cnt[n - 1][n - 1] == 0:
            return [0, 0]

        return [dp[n - 1][n - 1], cnt[n - 1][n - 1]]