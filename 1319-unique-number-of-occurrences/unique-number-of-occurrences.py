class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        new_list = []
        for num in arr:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1
        new_list = list(freq.values())
        for i in range (0, len(new_list)-1):
            for j in range (i+1, len(new_list)):
                if new_list[i] == new_list[j]:
                    return False
        return True




        