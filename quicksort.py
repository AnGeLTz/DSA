my_array = [1,3,6,7,2,9,23,18,0]

def quicksort(array):

	if len(array) <= 1:
		return array
	pivot = array[len(array) // 2]
	less = [i for i in array if i < pivot]
	middle = [i for i in array if  i == pivot]
	greater = [i for i in array if i > pivot]

	return quicksort(less) + middle + quicksort(greater)
sorted_array = quicksort(my_array)

print(sorted_array) 
