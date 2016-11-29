#1+2+3+....+100###############
sum=0
for i in range(1,101):
    sum+=i
print sum
##############################
###冒泡排序算法#################
def bubbleSort(arr):
    count = len(arr)
    for i in range(0,count):
        for j in range(i+1,count):
            if(arr[i]>arr[j]):
                tmp=arr[i]
                arr[i]=arr[j]
                arr[j]=tmp
    return arr
arr=[46,243,1,3,6,8,9]
k=bubbleSort(arr)
print k
##############################
#####选择排序算法###############
def select_sort(lists):
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        tmp=lists[min],
        lists[j] = lists[i],
        lists[i]=tmp

    return lists
arr=[46,243,1,3,6,8,9]
k=bubbleSort(arr)
print k
####################################
########插入排序#####################
def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]#要插入的数据
        j = i - 1    #已经排好的序列
        while j >= 0:
            if lists[j] > key: #从后往前比较，找到合适的位置插入
                lists[j + 1] = lists[j] 
                lists[j] = key
            j -= 1
    return lists
######################################
'''
1. 从第1个元素开始，该元素可认为已排序
2. 取下一个元素，对已排序数组从后往前扫描
3. 若从排序数组中取出的元素大于新元素，则移至下一位置
4. 重复步骤3，直到找到已排序元素小于或等于新元素的位置
5. 插入新元素至该位置
6. 重复2~5
'''
#####################################
############归并排序##################
def merge_sort(aList):  
    n = len(aList)  
    # 只有一个元素，“触底”了，直接返回  
    if n <= 1:  
        return aList  
                # 分割成两部分  
    mid = n // 2
    
    left = merge_sort(aList[:mid])  
    right = merge_sort(aList[mid:])
    print left
    print 'ssssssssssssssssssss'
    print right
    print 'dddddddddddddddddddd'
    # 合并  
    return merge_sort_helper(left, right)  
              
              
# 这个函数用来合并两个排好序的数组  
def merge_sort_helper(l1, l2):  
    result = []  
    index1 = index2 = 0  
    n1 = len(l1)  
    n2 = len(l2)  
    while index1 != n1 and index2 != n2:  
        if l1[index1] < l2[index2]:  
            result.append(l1[index1])  
            index1 += 1  
        else:  
            result.append(l2[index2])  
            index2 += 1  
    result.extend(l2[index2:])  
    result.extend(l1[index1:])  
    return result  


a=[10,4,6,3,8,2,5,7]
k=merge_sort(a)
print k
#####################################
'''
归并就是先将数组分成两部分直至最简，然后用另一个函数处理最简得到结果返回，依次这样处理，最终的结果就是我们要得到的结果。
详细讲解：http://blog.csdn.net/guoziqing506/article/details/50949854
'''
#####################################
########桶排序#######################
def bucket_sort(aList):  
    n = len(aList)  
    result = [0 for i in range(n)]  
    for i in range(n):  
        result[aList[i] - 1] = aList[i]  
    return result  

def bucket_sort(aList):  
    n = len(aList)  
    for i in range(n):  
        # aList第i位不符合，一直执行此循环  
        while aList[i] != i + 1:  
            # 以下三行代码实现aList[i]与aList[aList[i] - 1]的交换  
            temp = aList[i]  
            aList[i] = aList[temp - 1]  
            aList[temp - 1] = temp 
######二分法查找######################
def binarySearch(self, nums, target):
        # write your code here
        low = 0
        height = len(nums)-1
        print height
        print '\n'
        while low <= height:
            mid = int((low+height)/2)
            print mid
            if nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                height = mid - 1

            else:
                return nums.index(target)
        return  (-1)

def main():
    l=[1,2,3,4,5,6,7,8,9,10]
    k=binarySearch(True,l,1)
    print k
#####################################
'''
  普通的二分查找只是针对无重复的有序序列，则再次会有些变形需要考虑总结：
  1.数组中含有重复元素有序序列，找到重复元素第一次出现的位置
  2.看数组中是否有这个元素，如果没有返回这个元素应该插在哪，此时只需返回最左侧的值即可
  3.二维矩阵搜查目标数，前提是这个二维矩阵不管列与行都是有序的。
'''
##########################################
class Solution:  
    # @param nums: The integer array  
    # @param target: Target number to find  
    # @return the first position of target in nums, position start from 0   
    def binarySearch(self, nums, target):  

        left, right = 0, len(nums) - 1  

        while left <= right:  
            mid = (left + right) // 2  
            # 即便nums[mid] == target，也要继续查左边的部分  
            if nums[mid] >= target:  
                right = mid - 1  
            else:  
                left = mid + 1  

        if left <= len(nums) and nums[left] == target:  
            return left  

        return -1  
'''
当找到重复元素时，不一定就是我们要找的第一次出现的位置，按排序它一定在小于等于mid这一次还有，而且最终肯定是num[left]==target,
注意越界条件
'''
##############################################
'''
写出一个高效的算法来搜索 m × n矩阵中的值。这个矩阵具有以下特性：每行中的整数从左到右是排序的.每行的第一个数大于上一行的最后一个整数
样例：
考虑下列矩阵：
[
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

给出 target = 3，返回 true
'''
class Solution:  
    """ 
    @param matrix, a list of lists of integers 
    @param target, an integer 
    @return a boolean, indicate whether matrix contains target 
    """  
    def searchMatrix(self, matrix, target):  
        row = len(matrix)  
        if row == 0:  
            return False  
        col = len(matrix[0])  
        # left,right代表列数  
        left, right = 0, col - 1  
        # high,low代表行数  
        high, low = row - 1, 0  
        while low <= high:  
            mid1 = (low + high) // 2  
            if matrix[mid1][0] == target:  
                return True  
            if matrix[mid1][0] > target:  
                high = mid1 - 1  
            if matrix[mid1][0] < target:  
                low = mid1 + 1  
        # 上面的循环结束后，low-1为target所在的行  
        while left <= right:  
            mid2 = (left + right) // 2  
            if matrix[low - 1][mid2] == target:  
                return True  
            if matrix[low - 1][mid2] > target:  
                right = mid2 - 1  
            if matrix[low - 1][mid2] < target:  
                left = mid2 + 1  
        return False  
      
