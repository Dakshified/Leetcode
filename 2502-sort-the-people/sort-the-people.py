class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        bauna = list(zip(names, heights))
        messi = sorted(bauna, key=lambda x: x[1], reverse=True)
        argentina = []
        for name, height in messi:
            argentina.append(name)
        return argentina