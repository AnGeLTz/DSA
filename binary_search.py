my_array = [0,1,2,3,4,5,6,7,8,9]

def binary_search(array,n):
	min_index  = 0
	max_index = len(array) - 1
	while min_index < max_index:
		mid = (max_index + min_index)//2
		if array[mid] == n:
			print(mid)
			return
		elif n > array[mid]:
			min_index = mid + 1
			print(min_index)

		elif n < array[min]:
			max_index = mid - 1
			print(max_index)
	print("The number does not exist in the list")
binary_search(my_array,10)
