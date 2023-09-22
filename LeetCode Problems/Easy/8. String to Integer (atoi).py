class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        s = s.strip()
        if not s:
            return 0

        i = 0
        sign = 1

        if s[0] in ['+', '-']:
            if s[0] == '-':
                sign = -1
            i += 1

        num = 0
        while i < len(s) and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1

        return num * sign
