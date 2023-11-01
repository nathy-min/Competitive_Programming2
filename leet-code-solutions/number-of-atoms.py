class Solution:
    def countOfAtoms(self, formula: str) -> str:
        dt = defaultdict(int)
        stack = [1]
        digits = ""
        lowers = ""
        for element in formula[::-1]:
            if element.isdigit():
                digits = element + digits
            elif element.islower():
                lowers = element + lowers
            elif element == ")":
                stack.append(stack[-1]*int(digits or 1))
                digits = ""
            elif element == "(":
                stack.pop()
            #if element is an uppercase letter
            else:
                element = element + lowers
                dt[element] = dt[element]+stack[-1]*(int(digits or 1))
                digits = ""
                lowers = ""
        result = []
        for key, value in sorted(dt.items()):
            if value == 1:
                value = ""
            result.append(key)
            result.append(str(value))
        return "".join(result)