class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        ans = 1
        cur = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                cur = 1
            ans = max(ans, cur)

        a = b = c = 0

        ab = {(0, 0): -1}
        ac = {(0, 0): -1}
        bc = {(0, 0): -1}
        abc = {(0, 0): -1}

        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1

            state = (a - b, c)
            if state in ab:
                ans = max(ans, i - ab[state])
            else:
                ab[state] = i

            state = (a - c, b)
            if state in ac:
                ans = max(ans, i - ac[state])
            else:
                ac[state] = i

            state = (b - c, a)
            if state in bc:
                ans = max(ans, i - bc[state])
            else:
                bc[state] = i

            state = (a - b, a - c)
            if state in abc:
                ans = max(ans, i - abc[state])
            else:
                abc[state] = i

        return ans