class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        extra=1
        index=len(digits)-1
        while extra==1 and index>=0:
            if digits[index]==9:
                digits[index]=0
                index-=1
            else:
                digits[index]=digits[index]+1
                extra=0
        if extra==1:
            digits.insert(0,1)
        return digits
        

