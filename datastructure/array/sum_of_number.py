#

# Problem statement, take dynamic array and do sum of given numbers in array

#

def get_input_end_user():
	n_array_length = int(input("enter the length of array"))
	input_array = []
	for i in range(0,n_array_length):
		number = int(input())
		input_array.append(number)

	print(input_array)
	print("perform sum of input array")

	sum_of_array_numbers(input_array,n_array_length)


def sum_of_array_numbers(input_array, n_array_length):
	sum_of_numbers = 0

	for i in range(0, n_array_length):
		sum_of_numbers = sum_of_numbers + input_array[i]

	print("so sum of given input array is", sum_of_numbers)


if __name__ == "__main__":
	get_input_end_user()