# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?


def mult_except(input_list):
    result = [None for i in range(len(input_list))]
    for idx in range(0, len(input_list)):
        temp = input_list.copy()
        del temp[idx]
        result[idx] = mult_list(temp)

    return result


def mult_list(input_list):
    result = 1
    for num in input_list:
        result = result * num
    return result


print(mult_except([1, 2, 3, 4, 5]))
print(mult_except([3, 2, 1]))
