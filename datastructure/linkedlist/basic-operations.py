class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Linkedlist:
	def  __init__(self):
		self.head = None


	def insert_data_at_begining(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node


	def traverse_list(self):
		current = self.head
		while current:
			print(current.data, end=" -> ")
			current = current.next
		print("None")


def create_linked_list():
	create_list = Linkedlist()
	print("enter the length of list")
	length_of_list = int(input())


	print("enter the numbers in list")
	for i in range(0, length_of_list):
		number = int(input())
		create_list.insert_data_at_begining(number)


	print("Linked List: ")
	create_list.traverse_list()



if __name__ == "__main__":
	create_linked_list()


