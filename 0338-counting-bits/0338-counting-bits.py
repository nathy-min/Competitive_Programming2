class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        m_b = 1
        for i in range(1,n + 1):
            if i & (m_b << 1):
                m_b = m_b << 1
            
            ans.append(ans[i - m_b] + 1)
        
        return ans
            