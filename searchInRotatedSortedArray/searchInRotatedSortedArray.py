class Solution:
    def search(self, nums, target):
        if (not nums):
            return(-1)
        left = 0
        right = len(nums) - 1
        while (left < right):
            mid = int(left + (right - left) / 2)
            if (nums[right] < nums[mid]):
                left = mid + 1
            else:
                right = mid

        if (target <= nums[len(nums) - 1]):
            right = len(nums) - 1
        else:
            left = 0

        while (left <= right):
            mid = int(left + (right - left) / 2)
            if (nums[mid] == target):
                return(mid)
            elif (nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1

        return(-1)
