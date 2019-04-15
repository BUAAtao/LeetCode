class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if (not s1) or s1_len > s2_len:
            return False
        # 字典存放不同字母出现次数
        target_num = {}
        temp_num = {}
        # 生成目标字典，和初始化临时字典
        for char in s1:
            if char in target_num.keys():
                target_num[char] += 1
            else:
                target_num[char] = 1
                temp_num[char] = 0
        # 扫描 s2 ，当最近的字典和目标字典相同时匹配。
        i = 0
        while i < s2_len:
            if s2[i] in temp_num.keys():
                temp_num[s2[i]] += 1
            if i >= s1_len and s2[i-s1_len] in temp_num.keys():
                temp_num[s2[i-s1_len]] -= 1
            if temp_num == target_num:
                return True
            i += 1            
        return False
