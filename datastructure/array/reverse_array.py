def get_input():
	length_of_array = int(input("Enter length of array"))
	print("Enter numbers in array")
	original_array = []
	for i in range(0, length_of_array):
		element = int(input())
		original_array.append(element)
	print("The original array: ", original_array)
	reverse_original_array(original_array)

def reverse_original_array(original_array):
	reverse_original_array = []
	for i in range(0, len(original_array)):
		element = original_array[len(original_array)-1-i]
		reverse_original_array.append(element)
	print("The reverse array: ",reverse_original_array)



if __name__ == "__main__":
	get_input()