from typing import List


def secondLargest(nums: List[int]):
    if len(nums) < 2:
        return "Not enough elements"

    largest = second_largest = float("-inf")  # -inf means the most negative value
    # Can take as the smallest value

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float("-inf"):
        return "There is no second largest element"
    else:
        return second_largest


nums = [12, 74, -89, 96, -98, -96, 52]
result = secondLargest(nums)
print(f"Second largest element = {result}")
