class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, l = [], 0
        i = 0

        while i < len(words):
            if len(line) + l + len(words[i]) > maxWidth:
                extra_spaces = maxWidth - l
                spaces = extra_spaces // max(1, len(line) - 1)
                r = extra_spaces % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if r:
                        line[j] += " "
                        r -= 1
                res.append(''.join(line))        
                line, l = [], 0

            
            line.append(words[i])
            l += len(words[i])
            i += 1

        spaces = maxWidth - l
        for i in range(len(line)):
            if spaces:
                line[i] += " "
                spaces -= 1

        line[-1] += " " * spaces
        res.append("".join(line))    

        return res    