"""
lab_1c.py

Given a list of numbers, return the maximum sum of any contiguous subarray of the list.

Do not assume anything. Account for all edge cases.

Derived from LeetCode problem: https://leetcode.com/problems/maximum-subarray/ (leetcode medium)
"""

# TODO: Find and resolve the bug in the following implementation. Create unit tests to verify your fix.
def max_subarray_sum(nums: list[int]) -> int:
    """
    Function that takes in a list of integers and returns the maximum sum of any contiguous subarray.

    Args:
        nums (list[int]): List of integers.

    Returns:
        int: The maximum sum of any contiguous subarray.
    """

    max_current = max_global = nums[0]
    
"""
TODO: implement function

for every index where number is nums[index]
    if the number is the first index:
        add the next index
        if it is bigger than max, continue and set max_global to it
        else break
    if the number is the last index:
        add the index before
        if it is bigger than max, continue and set max_global to it
        else break
    if the number is the middle index:
        for dir in [-1, 1]:
            int current_displacement = 1
            try:
                next_num = nums[index + current_displacement * dir]
                max_current = max of max_current and number + next_num
                continue by current_displacement++
            else:
                max_global = max(max_current, max_global)
                break
    
    return max_global
"""    

# Example usage:
def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = max_subarray_sum(nums)
    print(f"Maximum subarray sum: {result}")

if __name__ == "__main__":
    main()