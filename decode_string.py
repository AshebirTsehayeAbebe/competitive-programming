class Solution:
    def decodeString(self, s: str) -> str:        
        def decode(index):
            digit=s[index]
            while s[index+1]!='[':
                digit+=s[index+1]
                index+=1
            cur = index
            if not s[index].isdigit():
                multiplier = 1
            else:
                multiplier = int(digit)
                cur += 2
            chars = []
            while cur < len(s) and s[cur] != ']':
                if s[cur].isalpha():
                    chars.append(s[cur])
                    cur += 1
                else:
                    decodedString, nextCur = decode(cur) # cc
                    chars.append(decodedString)
                    cur = nextCur        
            return multiplier*(''.join(chars)), cur+1
        
        cur = 0
        result = []
        while cur < len(s):
            if s[cur].isdigit():
                decoded, nextIndex = decode(cur)
                cur = nextIndex
                result.append(decoded)
            else:
                result.append(s[cur])
                cur += 1
        return ''.join(result)
