my_array = [1,2,3,4,5,6]

def min_max(array):
	min = array[0]
	max = array[0]
	for number in array:
		if number < min:
			min = number
		if number > max:
			max = number
	print(f"Min value {min}, Max value {max}")
min_max(my_array)
