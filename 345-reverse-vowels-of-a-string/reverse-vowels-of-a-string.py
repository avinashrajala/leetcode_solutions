class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        a = list(s)
        left=0
        right = len(a)-1
        while left < right:
            while left < right and a[left] not in vowels:
                left += 1
            while left < right and a[right] not in vowels:
                right -= 1
            a[left],a[right]=a[right],a[left]
            left += 1
            right -= 1
        return ''.join(a)        