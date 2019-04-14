class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        test = ''
        length = tmp = 0
        for i in s:
            if i not in test:
                test += i
                tmp = len(test)
                length = max(tmp, length)
            else:
                index = test.index(i)
                test = test[index+1:] + i
        return length
