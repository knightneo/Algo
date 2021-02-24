#!/usr/bin/python
# -*- coding:utf8 -*-

#插入排序(Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

#堆排序(Heap Sort)
def heap_sort(arr):
    #最大堆调整:max heapify
    #将堆的末端子节点作调整，使得子节点永远小于父节点
    def max_heapify(start_index, end_index):
        root_index = start_index
        while True:
            #每轮循环中,处理root_index为根结点的子树
            #左子树的索引
            left_child_index = (root_index << 1) + 1
            #如果是叶子结点,直接终止循环
            if left_child_index > end_index:
                break;
            #找出最大的子节点索引
            right_child_index = left_child_index + 1
            max_index = left_child_index
            if right_child_index <= end_index and arr[left_child_index] < arr[right_child_index]:
                max_index = right_child_index
            #如果子节点更大则交换位置
            if arr[root_index] < arr[max_index]:
                arr[root_index], arr[max_index] = arr[max_index], arr[root_index]
                root_index = left_child_index
            else:
                break;

    #创建最大堆:build max heap
    #遍历非叶子结点
    #子节点i的父节点位置(i-1) >> 1
    #遍历的起始结点为最右非叶子结点
    #即最后一个结点的父节点
    #最后一个结点的索引为len(arr) - 1
    #遍历的最后一个结点为根结点,索引为0
    start_index = (len(arr) - 2) >> 1
    for start in xrange(start_index, -1, -1):
        max_heapify(start, len(arr) - 1)

    #堆排序:heap_sort
    #此时最大堆的root结点已经是最大值,所以把根结点取出来,用最后一个结点填充到根结点重新调整一个最大堆
    #移除的根结点填充到数组的尾部作为最大值
    for end in xrange(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        max_heapify(0, end - 1)

    return arr

#快速排序(Quick Sort)
#O(n*(log n))
#消耗额外内存版本O(n)
#(最好写)
def quick_sort_v1(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x > pivot]
    arr = quick_sort(less) + [pivot] + quick_sort(greater)
    return arr
#原地交换版本O(log n)
#(写起来麻烦)
def quick_sort_v2(arr):
    if len(arr) <= 1:
        return arr
    def partition(sub, left, right, pivot_index):
        pivot = sub[pivot_index]
        #pivot移到末尾
        sub[pivot_index], sub[right] = sub[right], sub[pivot_index]
        store_index = left
        #小于pivot的放在store_index左边,大于pivot放在store_index右边
        for i in range(left, right):
            if sub[i] <= pivot:
                sub[store_index], sub[i] = sub[i], sub[store_index]
                store_index += 1
        #把pivot放在store_index的位置,此时pivot左边都比他小,pivot右边都比他大
        sub[right], sub[store_index] = sub[store_index], sub[right]
        return store_index
    def sort(sub, left, right):
        if left < right:
            pivot_index = left;
            new_pivot_index = partition(sub, left, right, pivot_index)
            sort(sub, left, new_pivot_index - 1)
            sort(sub, new_pivot_index + 1, right)
    sort(arr, 0, len(arr) - 1)
    return arr





            

arr = [5,2,3,1,4]
#quick_sort(arr)
print('sorted array:')
print(quick_sort_v2(arr))
