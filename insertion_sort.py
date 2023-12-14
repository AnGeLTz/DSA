from execution_time_decorator import measure_time
my_array = [1,2,3,4,5,6]

@measure_time
def insertion_sort(array):
	for i in range(1,len(array)):
		key = array[i]
		j = i-1
		while array[j] <  key and j >=0:
			array[j+1] = array[j]
			j-=1
		array[j+1] = key
	print(array)
insertion_sort(my_array)
