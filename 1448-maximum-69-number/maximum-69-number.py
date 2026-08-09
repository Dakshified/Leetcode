class Solution:
    def maximum69Number (self, num: int) -> int:
        new_num=int(str(num).replace('6', '9', 1))
        return new_num 

