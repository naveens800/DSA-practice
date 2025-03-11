def isValid(s: str) -> bool:
        if s and s[0] in ['}', ']', ')']:
            return False
        if len(s) == 1: return False
        d = {'}':'{', ']':'[', ')':'('}
        q = list()
        for char in s:
            if char in ['}', ']', ')'] and q:
                item = q.pop()
                if d[char] != item:
                    return False
            else:
                q.append(char)
        if q:
            return False

        return True


if __name__ == '__main__':
    print(isValid('{{}}[[]]'))
    print(isValid('{}}}}[][]'))
    print(isValid('{{[[[]]]}}'))