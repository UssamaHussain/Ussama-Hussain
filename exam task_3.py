def largest_subarray(nums):
    if not nums:
        return 0

    # initializing all variables equal to the first element of the array
    current_max = current_min = largest_product = nums[0]

    #  iterating over each element in the subarray of nums starting from the second element
    for num in nums[1:]:
        # if num < 0 changing max to min
        if num < 0:
            temp = current_max
            current_max = current_min
            current_min = temp

        # gets the max from num and num*current_max
        temp_max = max(num, current_max * num)
        # gets the min from num and num*current_min
        temp_min = min(num, current_min * num)

        current_max = temp_max
        current_min = temp_min

        # comparing existing largest one with the current
        largest_product = max(largest_product, current_max)

    return largest_product


# Test cases
print(largest_subarray([2, 3, -2, 4]))  # Output: 6
print(largest_subarray([-2, 0, -1]))  # Output: 0
