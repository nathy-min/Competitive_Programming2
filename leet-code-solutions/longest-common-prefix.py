class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.children[ord(c) - 97]:
                curr.children[ord(c) - 97] = TrieNode()
                curr.children[-1] += 1
            curr = curr.children[ord(c) - 97]    
        curr.is_end = True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        i = 0
        for st in strs:
            if not st:
                return ""
            self.insert(st)
        curr = self.root

        while curr.children[-1] < 2:
            s += strs[0][i]
            temp = curr.children[ord(strs[0][i]) - 97]
            if temp.is_end:
                break
            curr = temp
            i += 1

        return s        
        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]        
        self.children.append(0)