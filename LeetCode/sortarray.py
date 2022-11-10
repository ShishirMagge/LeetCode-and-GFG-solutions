class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num0 = nums.count(0)
        num1 = nums.count(1) + num0
        num2 = nums.count(2) + num1

        for i in range(len(nums)):
            if i < num0:
                nums[i] = 0
            elif i < num1:
                nums[i] = 1
            elif i < num2:
                nums[i] = 2
