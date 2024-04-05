class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000, 
        }

        sum = 0

        for i in range(len(s)):
            roman_value = my_dict.get(s[i])
            if not roman_value:
                return None
            if i < len(s) - 1 and roman_value < my_dict.get(s[i + 1]):
                sum -= roman_value
            else:
                sum += roman_value
        return sum
    
st = Solution()
print(st.romanToInt("MCMXCIV"))