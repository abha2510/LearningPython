def find_two_sum(array, target):
    complement_dict = {}

    for i, num in enumerate(array):
        complement = target - num

        if complement in complement_dict:
            return [complement_dict[complement], i]
        else:
            complement_dict[num] = i

    return "No two elements sum up to the target"


array = [2, 7, 11, 15]
target = 9
result = find_two_sum(array, target)
print(result)
