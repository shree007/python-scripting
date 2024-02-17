

def check_number_exist_in_array():
	input_array=get_input_for_array()
	print(input_array)
	print("enter the number to search")
	search_number = get_number_which_need_to_search()
	search_number_in_array(input_array, search_number)



def get_input_for_array():
	print("enter the length of input_array")
	n_array_length = int(input())
    
	print("input the number in array")
	input_array = []

	for i in range(0,n_array_length):
		element = int(input())
		input_array.append(element)

	return input_array


def get_number_which_need_to_search():
	return int(input())

def search_number_in_array(input_array, search_number):
	check_point = False
	for i in range(0, len(input_array)):
		if input_array[i] == search_number:
			print("yes it is exist at postion",i)
			check_point=True
	if check_point == False :
		print("it is not in input_array, thanks, better luck to next time")
	


if __name__ == "__main__":
	check_number_exist_in_array()