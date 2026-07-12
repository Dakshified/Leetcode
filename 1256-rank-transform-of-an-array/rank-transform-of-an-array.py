class Solution:
    def arrayRankTransform(self, arr):
        # Sort unique elements
        sorted_unique = sorted(set(arr))

        # Map each value to its rank
        rank = {}
        for i, num in enumerate(sorted_unique):
            rank[num] = i + 1

        # Build the answer
        return [rank[num] for num in arr]