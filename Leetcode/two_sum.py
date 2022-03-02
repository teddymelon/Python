#第一種用迴圈暴力解法
from difflib import diff_bytes


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                if nums[a] + nums[b] == target:
                    return (a,b)


#第二種用HashMap(Dict)的方式來解，主要是用 target - nums[i]，然後判斷是否有存在在這個Hashmap裡面。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict() #key:差值 ; value:index
        for i in range(len(nums)):
            if nums[i] in diff:
                return (diff[nums[i]], i)  #要倒過來想，同時使用dict[key]，會回傳dict的value。
            else:
                diff[target-nums[i]] = i   # i會等於 0,1,2,3,4...，所以相當於key值變成 tartget - nums[i]，然後Value則是的位置。