class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m % MOD

        # length = 2
        up = [0] * m
        down = [0] * m

        for v in range(m):
            up[v] = v
            down[v] = m - 1 - v

        if n == 2:
            return sum(up) % MOD

        for _ in range(3, n + 1):
            prefix_down = [0] * (m + 1)
            for i in range(m):
                prefix_down[i + 1] = (prefix_down[i] + down[i]) % MOD

            suffix_up = [0] * (m + 1)
            for i in range(m - 1, -1, -1):
                suffix_up[i] = (suffix_up[i + 1] + up[i]) % MOD

            new_up = [0] * m
            new_down = [0] * m

            for v in range(m):
                new_up[v] = prefix_down[v]               # sum of down[u], u < v
                new_down[v] = suffix_up[v + 1]          # sum of up[u], u > v

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD