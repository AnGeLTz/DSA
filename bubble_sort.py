from execution_time_decorator import measure_time

my_array = [1,2,3,4,5,6]

@measure_time
def bubble_sort_desc(array):
	max_swaps = len(array) - 1
	for i in  range(max_swaps):
		for j in range(len(array) - 1):
			if array[j+1] > array[j]:
				temp = array[j]
				array[j] = array[j+1]
				array[j+1]=temp
	print(array)

bubble_sort_desc(my_array)
