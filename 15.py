class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_dict = {}
        result = []
        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1
        pos = [i for i in num_dict if i>0]
        neg = [i for i in num_dict if i<0]
        neg.sort()

        if 0 in num_dict and num_dict[0]>=3:
            result.append([0,0,0])
        for i in pos:
            for j in neg:
                k = -i-j
                if k in num_dict:
                    if(k==i or k==j) and num_dict[k]>=2:
                        result.append([j,k,i])
                    elif j<k<i:
                        result.append([j,k,i])
                    if k<j:
                        break
        return result

#本人超时版本1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        re = []
        tmp = nums[:]
        for i in range(len(nums)-2):
            last = tmp.pop()
            target = 0 - last
            for j in range(len(tmp)-1):
                if target-tmp[j] in tmp[j+1:]:
                    ls = [tmp[j], target-tmp[j], last]
                    if ls not in re:
                        re.append(ls)
        return re
#超时版本2
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        re = []
        for i in range(len(nums)-2):
            for j in range(len(nums)-i-2):
                if 0-nums[i]-nums[i+j+1] in nums[i+j+2:]:
                    tmp = sorted([nums[i],nums[i+j+1],0-nums[i]-nums[i+j+1]])
                    if tmp not in re:
                        re.append(tmp)
        return re
