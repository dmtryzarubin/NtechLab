a = input('Введите массив чисел через запятую, например : 56,65,-2,0 \nМассив: ')
a = list(a.split(','))
a = [int(i) for i in a]

def ﬁndMaxSubArray(nums):
    max_so_far = nums[0]
    max_ending_here = nums[0]
    start, stop = 0, 0
    
    for i in range(1, len(nums)):
        if (max_ending_here + nums[i]) > nums[i]:
            max_ending_here = max_ending_here + nums[i]
        elif max_ending_here + nums[i] <= nums[i]:
            max_ending_here  = nums[i]
            start = i
        if max_so_far <= max_ending_here:
            max_so_far = max_ending_here
            stop = i
    return nums[start:stop+1]

print (ﬁndMaxSubArray(a))