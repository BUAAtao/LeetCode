#自己解法，按照解题思路二所写
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        rs = ''
        if numRows == 1:
            row = l
        else:
            row = l//(2*numRows-2) + 1
        for i in range(numRows):
            for j in range(row):
                if i == 0:
                    if numRows == 1:
                        rs += s[j]
                    elif j*(2*numRows-2) < l:
                        rs += s[j*(2*numRows-2)]
                elif i == numRows - 1:     #多层判断注意elif使用
                    if j*(2*numRows-2) + numRows - 1 < l:
                        rs += s[j*(2*numRows-2) + numRows - 1]
                else:
                    if j*(2*numRows - 2) + i < l:
                        rs += s[j*(2*numRows - 2) + i]
                    if (j+1)*(2*numRows - 2) - i < l:
                        rs += s[(j+1)*(2*numRows - 2) - i]
        return rs

#题解思路一
class Solution(object): 
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        L = [''] * numRows
        index, step = 0, 1
        for x in s:
            L[index] += x   
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step
        return ''.join(L)

