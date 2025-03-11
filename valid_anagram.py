def isAnagram(s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for char in s:
            d[char] = d.get(char, 0) + 1
        
        for char in t:
            if char not in d:
                return False
            d[char] -= 1
            if d[char] == 0:
                del d[char]
        if not d:
            return True


if __name__ == '__main__':
    print(isAnagram('racecar', 'carrasce'))