# Returns the square of a number if it's odd; otherwise, returns the original number.
def square_if_odd(num): 
    # TODO: implement this!
    if num%2 == 1:
        print("Odd")
        num = num*num
    else:
        print("Even")
    print(num)
    return num


# Returns whether the given number is within the range of lower and upper inclusive (True or False).
def in_range(lower, upper, num):
    # TODO: implement this!
    print("(lower, upper, num) = ", lower, upper, num)
    if num >= lower and num <= upper:
        print("True")
        return True
    else:
        print("False")
        return False


# Takes in a list of numbers and returns a list of only the even ones.
def even_elements(nums):
    # TODO: implement this!
    even_nums = []
    for num in nums:
        if num%2==0:
            even_nums.append(num) 
    print("even_nums = ", even_nums)
    return even_nums

# Need these routines from L03:

# Prints out each corresponding key/value pair in a dict.
def dict_print(d):
    for key, value in d.items():
        print("key: " + str(key) + " value: " + str(value))

# Returns the key that has the highest value in the dict.
# (You can assume all values in the dict are positive numbers.)
def key_max_value(d):
    # TODO: finish this!
    max = 0
    key_max = 0
    for key, value in d.items():
        print("key: " + str(key) + " value: " + str(value))
        if value > max:
            print("Found a new max = " + str(value) + " at key = " + str(key))
            max = value
            key_max = key
    return key_max

# Takes in a string and returns the most common letter occuring in the string.
# If there's a tie, you may return any of them.
def most_common_letter(str):
    # TODO: implement this!
    # Python3 code to demonstrate  
    # each occurrence frequency using  
    # naive method  
  
    # using naive method to get count  
    # of each element in string  
    all_freq = {} 
  
    for i in str: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
  
    # printing result  
    # print ("Count of all characters in GeeksforGeeks is :\n " +  all_freq) 
    dict_print(all_freq)

    key_max_value(all_freq)

    return key_max_value(all_freq)


# Takes in a list of numbers and returns the maximum difference between any two numbers in the list.
    

def max_diff(nums):
    # TODO: implement this!
    cur_min = nums[0]
    cur_max = nums[0]
    for num in nums:
        if num > cur_max:
            cur_max = num
        if num < cur_min:
            cur_min = num
    print("cur_max = ", cur_max, "cur_min = ", cur_min, "max_diff = ", cur_max - cur_min)
    return cur_max - cur_min

# Prints an hourglass made out of '*' characters with a base the size of the number supplied * 2.
def hourglass(size):
    # TODO: implement this!
    line_length = size
    while line_length > 0:
        asterisk_count = 0
        while asterisk_count < line_length:
            print("x")
            asterisk_count = asterisk_count + 1
        line_length = line_length - 1

hourglass(3)







'''
The below code is just to test your code. You don't need to touch these.
'''

def test_function(fn, tests):
    print("Testing %s..." % fn.__name__)
    for i, (args, expected_result) in enumerate(tests):
        print("Running test %d (%r)..." % (i, args))
        if not isinstance(args, tuple):
            args = (args,)
        actual_result = fn(*args)
        if actual_result == expected_result:
            print("PASS!")
        else:
            print("FAIL!")
            print("result was %r, but it should have been %r" % (actual_result, expected_result))
            return False
    return True

fn_to_tests = [
    (square_if_odd, [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 9),
        (-8, -8),
        (-9, 81),
    ]),
    (in_range, [
        ((0, 0, 0), True),
        ((1, 3, 2), True),
        ((-2, 80, 80), True),
        ((-3, 5, 6), False),
    ]),
    (even_elements, [
        ([1, 2, 5, 7, 2, 6, 7, 9], [2, 2, 6]),
        ([-8, 2, 4], [-8, 2, 4]),
        ([1, 3, 5, 7], []),
    ]),
    (most_common_letter, [
        ("abcb", "b"),
        ("popular", "p"),
        ("andskfjngrkejnhkjjfjfjnfnkzzjj", "j"),
    ]),
    (max_diff, [
        ([1, 4, -9, 2, 3, 20], 29),
        ([1, 3, 5], 4),
        ([-2, 0], 2),
    ]),
]

if __name__ == "__main__":
    for fn, tests in fn_to_tests:
        test_function(fn, tests)
        print()
