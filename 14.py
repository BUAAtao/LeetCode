class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

#本人解法第一次
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        test = ''
        l = len(strs[0])
        for nodes in strs:
            l = min(len(nodes),l)
        for i in range(l):
            tmp = strs[0][i]
            for nodes in strs:
                if tmp != nodes[i]:
                    return test
            test += tmp
        return test
