# Скрипт для нахождения подмассива с наибольшей сумме в массиве.
# ввод массива
a = input('Введите массив чисел через запятую, например : 56,65,-2,0 \nМассив: ')
a = list(a.split(','))
a = [int(i) for i in a]

# Реализован алгоритм Кадана
def ﬁndMaxSubArray(A):
    max_so_far = A[0] 
    max_ending_here = A[0] 
    start, stop = 0, 0
    
    for i in range(1, len(A)):
        if (max_ending_here + A[i]) > A[i]:
            max_ending_here = max_ending_here + A[i]
        elif max_ending_here + A[i] <= A[i]:
            max_ending_here  = A[i]
            start = i
        if max_so_far <= max_ending_here:
            max_so_far = max_ending_here
            stop = i

    return A[start:stop+1]

print (ﬁndMaxSubArray(a))