class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one = 1
        i = 0
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                    i += 1
                else:
                     digits[i] +=1
                     one = 0
            else:
                digits.append(one)
                one = 0
                i += 1
        return digits[::-1]
    '''
    here my approach was very simple that we have to add number in a array in such way that we can take carry
    '''