class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        set1 = set(sentence)
        if(len(set1)== 26):
            return True
        else:
            return False
        