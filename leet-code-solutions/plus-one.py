class Solution:

    def plusOne(self, digits):

        """

        :type digits: List[int]

        :rtype: List[int]

        """

        p=0

        num1=0

        for i in range (len(digits)-1,-1,-1):

            num1+=digits[i]*10**p

            p+=1

        num1+=1

        return [int(i) for i in str(num1)]

    
    
    
    
        