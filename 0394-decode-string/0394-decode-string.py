class Solution:
    def decodeString(self, s: str) -> str:
        def decode(ptr, string, nums):
            if ptr == len(s):
                return string[0]
            temp = string
            if s[ptr].isdigit():
                if nums[-1] == "#":
                    nums.append(s[ptr])
                else:
                    nums[-1] += s[ptr]
                 
                return  decode(ptr + 1, string, nums)          
                
            elif s[ptr] == "[":
                nums.append("#")
                string.append("")
                return decode(ptr + 1, string, nums)
            elif s[ptr] == "]":
                nums.pop()
                temp = string.pop()
                string[-1] += int(nums.pop()) * temp
                return decode(ptr + 1, string, nums)
            else:
                string[-1] += s[ptr]
                return decode(ptr + 1, string, nums)
                
        return decode(0, [""], [" ","","",""])        