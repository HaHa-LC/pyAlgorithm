# -*- coding: utf-8 -*-

def sum(list):
	if list==[]:
		return 0
	return list[0]+sum(list[1:])
	
def count(list):
	if list==[]:
		return 0
	return 1+count(list[1:])

#这个相对没有前2个好理解，注意其基线条件和递归条件
def max(list):
	if len(list)==2:
		return list[0] if list[0]>list[1] else list[1]
	sub_max=max(list[1:])
	return list[0] if list[0]>sub_max else sub_max
	
#快速排序代码
def quicksort(array):
	if len(array)<2:
		return array    #基线条件：为空或只包含一个元素的序列是“有序”的
	else:
		pivot=array[0]	#递归条件
		less=[i for i in array[1:] if i<=pivot]  	#由所有小于等于基准值的元素组成的子序列
		greater=[i for i in array[1:] if i>pivot]	#由所有大于基准值的元素组成的子序列
		
		return quicksort(less)+[pivot]+quicksort(greater)


print quicksort([10,5,2,3])		

	
print sum([2,4,6])
print count([2,4,6])
print max([2,4,6])