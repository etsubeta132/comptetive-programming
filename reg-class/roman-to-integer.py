class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        rom_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        l = 0
        while l<len(s):
            if l+1 < len(s):
                if rom_dict[s[l]]<rom_dict[s[l+1]]:
                    result= result + rom_dict[s[l+1]]-rom_dict[s[l]]
                    l+=2
                else:
                    result+=rom_dict[s[l]]
                    l+=1
            else:
                result+=rom_dict[s[l]]
                l+=1
        return result
