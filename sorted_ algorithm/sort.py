'''
基础排序算法练习
https://www.runoob.com/w3cnote/bubble-sort.html
'''

'''
1.冒泡排序:
每一次比对相邻的两个元素，一轮后，会把最大的元素放到最后面
如此循环
'''


from operator import le
from turtle import right

'''
冒泡排序
两两相邻元素开始比较，如果当前元素>后一个元素，则进行交互
每一轮遍历后，会找到一个最大的元素放在数组最后

'''
def bubble_sort(nums):
    for i in range(1,len(nums)):
        for j in range(0,len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
        print(nums)
    # print(nums)

'''
每一次找出最小的元素，放在第一位
'''
def my_sort(nums):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
        print(nums)
    # print(nums)


'''
2.选择排序：
每一次从未排序的数据中找出最小的元素放在已排好序的后面
'''
def selected_sort(nums):
    for i in range(0,len(nums)):
        min_index = i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[min_index]: #这里主要要和当前最小的元素进行比较，而不是nums[i]
                min_index = j
        if min_index != i:
            nums[i],nums[min_index] = nums[min_index],nums[i]
        print(nums)


'''
3.插入排序:想象一下打扑克牌场景
（1）、从第一个元素开始，该元素可以认为已经被排序
（2）、取出下一个元素，在已经排序的元素中从后向前扫描：current_val = nums[i],j=j-1
（3）、只要排序好的元素>当前元素，就把排序好的元素往后挪一位：nums[j+1]=nums[j]
（4）、重复步骤（3），直到找到已排序的元素小于或者等于新元素的位置:while j>=0 and nums[j]>current_val:j-=1
（5）、将新元素插入该位置后 nums[j+1]=current_val
（6）、重复步骤2-6：for i in range(1,len(nums))
'''
def insert_sort(nums):
    
    for i in range(1,len(nums)):
        current_val = nums[i]
        j = i - 1
        while j>=0 and nums[j] > current_val:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = current_val
        print(nums)


'''
4.希尔排序：
1、先将整个待排序的序列拆分成多个待排序的子序列分别进行直接插入排序

'''
def shell_sort(nums):

    step = len(nums)//2
    
    while step >0:

        for cur in range(step,len(nums)):
            i = cur
            while i>=step and nums[i-step]>nums[i]:
                nums[i-step],nums[i] = nums[i],nums[i-step]
                i -= step
        step = step//2
        print(nums)


'''
归并排序：
1、申请空间，大小为拆分为两个有序序列后的和，该空间用来存放合并后的序列
2、设定两个指针，最初位置分别为两个已经排序序列的初始位置
3、每次比较两个序列的元素，将小的元素放入排序序列中，指针下移
4、循环步骤3

'''

def merge_sort(nums):
    if(len(nums)<2):
        return nums
    mid = len(nums)//2
    left = nums[0:mid]
    right = nums[mid:]
    print("left:",left)
    print("right:",right)
    res = merge(merge_sort(left),merge_sort(right))
    print("res:",res)
    return res
            
def merge(left,right):
    res = []
    while left and right:
        if left[0] > right[0]:
            res.append(right.pop(0))
        else:
            res.append(left.pop(0))

    while left:
        res.append(left.pop(0))
    while right:
        res.append(right.pop(0))
    
    return res


'''
快速排序
'''
def quick_sort(nums,low,high):
    if low>=high:
        return 
    
    pivot = nums[low]
    i = low
    j = high

    while i < j:
        while i <j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]
            
        while i<j and nums[i] < pivot:
            i +=1
        nums[j] = nums[i]
    
    nums[j] = pivot
    quick_sort(nums,low,i-1)
    quick_sort(nums,i+1,high)

    

nums=[30,10,50,70,20,11,9,8,100,5,200,1]
# merge_sort(nums)
quick_sort(nums,0,len(nums)-1)
print(nums)


