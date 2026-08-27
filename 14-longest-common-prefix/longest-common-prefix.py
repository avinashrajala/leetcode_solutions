class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans =""
        V = sorted(strs)
        first = V[0]
        last = V[-1]
        for i in range(min(len(first),len(last))):
            if(first[i] != last[i]):
                return  ans
            ans += first[i]
        return ans
        