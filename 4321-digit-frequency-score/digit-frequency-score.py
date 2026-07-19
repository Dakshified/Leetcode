class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        number =[]
        frequency = {}
        new_list = []
        if n ==0:
            return 0
        while n> 0:
            dig = n%10
            n = n//10
            number.append(dig)
        for num in number:
            if num in frequency :
                frequency[num] = frequency[num] +1
            else:
                frequency[num] = 1
        new_list = [key * value for key,value in frequency.items()]
        sum = 0
        for product in new_list:
            sum = sum + product
        return sum
        
            