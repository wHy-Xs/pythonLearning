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

      
