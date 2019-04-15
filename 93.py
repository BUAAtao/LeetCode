class Solution:
    # s是字符串, times是第几次递归, 最多4次
    def four_times_recursive(self, s, times):
        res = []
        #前面取太多导致后面为空串或者前面取太短导致递归次数大于4次, 返回空列表
        if s == '' or times > 4:
            return res
        #首位是0的话只能取一位, 否则可以取1-3位
        end = 2 if s[0] == '0' else 4
        for i in range(1, end):
            #i不能超长度, 然后判断取的段是否合法
            if i <= len(s) and int(s[:i]) <= 255:
                ip = s[:i] if times == 4 else (s[:i] + '.')
                #第四块取完整个字符串的话, 直接加进返回列表里
                if times == 4 and i == len(s):
                    res.append(ip)
                #否则从后面的字符串再取一段
                else:
                    tail = self.four_times_recursive(s[i:], times + 1)
                    if len(tail) > 0:
                        for j in tail:
                            res.append(ip + j)
        return res

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.four_times_recursive(s, 1)
