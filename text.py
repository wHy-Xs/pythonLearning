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
##############################
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

      
