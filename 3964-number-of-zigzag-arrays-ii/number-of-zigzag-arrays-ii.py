class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # Initial vector U^(2)
        vec = [[i] for i in range(m)]

        # Transition matrix
        A = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                if i + j >= m:
                    A[i][j] = 1

        def mat_mul(X, Y):
            n1, n2, n3 = len(X), len(Y), len(Y[0])
            res = [[0] * n3 for _ in range(n1)]

            for i in range(n1):
                for k in range(n2):
                    if X[i][k] == 0:
                        continue
                    val = X[i][k]
                    for j in range(n3):
                        res[i][j] = (res[i][j] + val * Y[k][j]) % MOD
            return res

        p = n - 2

        while p:
            if p & 1:
                vec = mat_mul(A, vec)
            A = mat_mul(A, A)
            p >>= 1

        ans = sum(row[0] for row in vec) % MOD
        return (2 * ans) % MOD