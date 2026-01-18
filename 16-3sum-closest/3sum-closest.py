class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        if closest_sum == target:
            return target
        for i in range(len(nums) - 2):
            k = target - nums[i]
            j, n = i + 1, len(nums) - 1
            while(j != n):
                cur_result = nums[j] + nums[n]
                if cur_result == k:
                    return target
                if abs(cur_result - k) < abs(closest_sum - target):
                    closest_sum = nums[i] + nums[j] + nums[n]
                if cur_result < k:
                    j += 1
                else:
                    n -= 1
        return closest_sum
