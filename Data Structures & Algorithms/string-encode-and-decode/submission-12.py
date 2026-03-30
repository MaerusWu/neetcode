class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "&" + s
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        length = ""
        start = 0
        for i in range(len(s)):
            print(start)
            if i >= start:
                if s[i] == "&":
                    res.append(s[i+1: i+1+int(length)])
                    start = i+1+int(length)
                    length =""
                else: 
                    length += s[i]
        return res
                