from collections import Counter

def mean(nums):
    nums_sum = sum(nums)
    return nums_sum / len(nums)

def median(nums):
    nums.sort()
    if len(nums) % 2 == 1:
        ind = len(nums) + 1 / 2 - 1
        return nums[ind]
    else:
        ind1 = len(nums) // 2 - 1
        ind2 = len(nums) // 2
        divided = (int(nums[ind1]) + int(nums[ind2])) / 2
        return nums[ind1] + ' and ' + nums[ind2] + ' could be considered the median. Their mean is ' + str(divided)

def mode(nums):
    result = []
    cnt = Counter(nums).most_common()
    max_cnt = cnt[0][1]
    for set in cnt:
        if set[1] == max_cnt:
            result.append(set[0])
    return ', '.join(result)


print('Enter set of numbers (comma separated):')
numbers = input()
n_arr = numbers.split(',')

print('Enter function (mean, median or mode):')
func = input()

if func == 'mean':
    print(mean(n_arr))
elif func == 'median':
    print(median(n_arr))
elif func == 'mode':
    print(mode(n_arr))
else:
    print('Incorrect function')