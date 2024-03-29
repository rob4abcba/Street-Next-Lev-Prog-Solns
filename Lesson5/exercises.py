# Searches linearly through a sorted list of numbers (nums) for a number
# (target) and returns whether or not the list contains the number.
def linear_search(nums, target):
    for num in nums:
        if num == target:
            return True
    return False


# Uses binary search to look through a sorted list of numbers (nums) for a
# number (target) and returns whether or not the list contains the number.
def binary_search(nums, target):
    # TODO: implement this!
    l = 0
    r = len(nums)
    print("nums, target = ", nums, target)
    while l <= r: 
  
        mid = int(l + (r - l)/2)
        print("l, r, mid = ", l, r, mid)
        print("nums[mid] = ", nums[mid])
          
        # Check if target is present at mid 
        if nums[mid] == target: 
            return True 
  
        # If target is greater, ignore left half 
        elif nums[mid] < target: 
            l = mid + 1
  
        # If target is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return False


# Code below here just tests if your code works properly. You don't need to
# change any of this code.


def test_binary_search(nums, target, desired_result):
    if binary_search(nums, target) is desired_result:
        print("TEST SUCCESS on: " + str(nums))
    else:
        print("TEST FAILED on: " + str(nums))


test_binary_search([1, 2, 3, 6, 7, 10, 10, 10], 7, True)
test_binary_search([1, 6, 10, 10, 10], 7, False)
test_binary_search([], 20, False)
test_binary_search([-80, -60, -10, 0, 12, 13], -80, True)
test_binary_search([-80, -60, -10, 0, 12, 13], -79, False)
