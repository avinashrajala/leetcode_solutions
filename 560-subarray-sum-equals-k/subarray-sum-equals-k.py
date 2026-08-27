class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count =0
        sum=0
        d = dict()
        d[0] = 1
        for i in range(len(nums)):
            sum = sum + nums[i]
            count += d.get(sum-k,0)
            d[sum] = d.get(sum,0) + 1
        return count
        
        