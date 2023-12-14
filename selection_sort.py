my_array = [1,2,3,4,5,6]

def selection_sort(array):
	n = len(array)
	for i in  range(n):
		max_index = i
		for j in range(i+1,n):
			if array[j] > array[max_index]:
				max_index = j
		temp = array[max_index]
		array[max_index] = array[i]
		array[i] = temp
	print(array)
selection_sort(my_array)
