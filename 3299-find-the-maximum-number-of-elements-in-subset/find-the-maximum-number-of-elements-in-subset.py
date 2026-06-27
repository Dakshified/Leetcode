from collections import Counter

class Solution:
    def maximumLength(self, nums):
        cnt = Counter(nums)
        ans = 1

        # Handle 1 separately
        if 1 in cnt:
            ones = cnt[1]
            ans = max(ans, ones if ones % 2 else ones - 1)

        for x in cnt:
            if x == 1:
                continue

            cur = x
            length = 0

            while cnt[cur] >= 2:
                length += 2
                cur *= cur

                # Numbers grow extremely fast
                if cur > 10**18:
                    break

            if cnt[cur]:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans