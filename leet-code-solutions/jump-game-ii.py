class Solution:

    def jump(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """

        if len(nums) <= 1:

            return 0

        start = count = 0

        reach = nums[0]

        while start<len(nums) and start<=reach:

            count +=1

            if reach >= len(nums)-1:

                return count

            max_ = 0

            for i in range(start,reach+1):

                if i+nums[i]>max_:

                    max_ = i+nums[i]

                    start = i

            reach = max_

        return -1  
