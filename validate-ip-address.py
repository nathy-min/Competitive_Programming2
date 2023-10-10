class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        v6 = queryIP.split(':')
        if len(v6) == 8:
            allowed = set("abcdefABCDEF")
            
            for hexa in v6:
                if not 1 <= len(hexa) <= 4:
                    return "Neither"
                
                for char in hexa:
                    if not char.isalnum() or (char.isalpha() and char not in allowed):
                        return "Neither"
                    
            return 'IPv6'
        
        v4 = queryIP.split('.')
        print(v4)
        if len(v4) == 4:
            for part in v4:
                if not part:
                    return "Neither"
                
                for char in part:
                    if not char.isnumeric():
                        return "Neither"
                
                int_val = int(part)
                if str(int_val) != part or not 0 <= int_val <= 255:
                    return "Neither"
                
            return "IPv4"
        
        return "Neither"