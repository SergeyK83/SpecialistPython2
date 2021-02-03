# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.


a = [0,5,3,6,-10,2, 4,2,4,5,-88,0,8]
def bubble_sort(nums, reverse=False):
    step = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - step):
            if nums[i] < nums[i + 1] if reverse else nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        step += 1

b=[]
for i in range(len(a)):
    b.append(abs(a[i]))

bubble_sort(b)
c = b[-10:]

print(sum(c))
