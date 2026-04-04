class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        required = len(countT)
        formed = 0
        l, r, = 0, 0
        res = [-1, -1]
        resLength = float("inf")


        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in countT and countT[s[r]] == window[s[r]]:
                formed += 1

            while formed == required:
                if (r - l + 1) < resLength:
                    res=[l,r]
                    resLength = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    formed -= 1
                l += 1
            r += 1
        l, r = res

        return s[l:r+1] if resLength != float("inf") else ""



