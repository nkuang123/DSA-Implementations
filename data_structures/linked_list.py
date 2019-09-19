# Implementation and complexity analysis of a Linked List data structure

# Linked Lists are made up of nodes that consist of the data they are storing,
# and a pointer reference to the next node in the list (could be None).
class ListNode:

	def __init__(self, data):
		self.data = data
		self.next = None  # The node initially doesn't point to anything,
						  # which can be configured later.

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self, data):
		self.data = data

	def set_next(self, node):
		self.next = node

	def __repr__(self):
		return "ListNode, val = {}".format(self.val)

# Linked List Class Structure
class LinkedList:

	def __init__(self, head=None):
		self.head = head  # Linked List initially has no nodes.
		self.size = 0

	def insert_at_head(self, data):
		new_node = ListNode(data)
		new_node.set_next(self.head)
		self.head = new_node

		self.size += 1

	def insert_at_end(self, data):
		# We need to traverse to the last node of the list before adding.
		ptr = self.head 

		while (ptr.get_next()):
			ptr = ptr.get_next()

		# Now we're at the last node, let's add the new node
		ptr.set_next(ListNode(data))

		self.size += 1

	def delete(self, data):
		# Special case: Node to be deleted is the first node of the list.
		if (self.head.get_data() == data):
			self.head = self.head.get_next()
			self.size -= 1

			return

		# Traverse until we find the node with the given data
		ptr = self.head
		prev = None

		while (ptr.get_data() != data):
			prev = ptr
			ptr = ptr.get_next()

		# At this point, ptr is the data to be deleted
		prev.set_next(ptr.get_next())

		self.size -= 1

	def sort(self):
		# Implemented using merge sort.

		# Retrieves length of linked list starting at node.
		def get_length(node):
			length = 0
			while (node):
				node = node.get_next()
				length += 1
			return length

		# Sorts the lists based on data value.
		def merge_list(node_a, node_b):
			result = None

			if not node_a:
				return node_b
			if not node_b:
				return node_a

			if (node_a.get_data() > node_b.get_data()):
				result = node_b
				result.set_next(merge_list(node_a, node_b.get_next()))
			else:
				result = node_a
				result.set_next(merge_list(node_b, node_a.get_next()))

			return result

		# Wrapper than divides the input array into subarrays of n/2 size
		def merge_sort(node):
			# Base case: return the node if list is size 1
			if not (node.get_next()):
				return node

			# Determine midpoint of list
			first_head = node
			mid = get_length(first_head) // 2

			for _ in range(mid-1):
				first_head = first_head.get_next()

			# Split list into 2 halves
			second_head = first_head.get_next()
			first_head.set_next(None)
			first_head = node

			# Recursively split
			t1 = merge_sort(first_head)
			t2 = merge_sort(second_head)

			# And merge
			return merge_list(t1, t2)

		self.head = merge_sort(self.head)

		# Complexity Analysis: Classic divide-and-conquer algorithm. The divide
		# step is just computing the midpoint, which takes O(1) time. The 
		# conquer part recursively sorts two subarrays of size n/2. Then we 
		# merge n elements, resulting in O(n) time. As we can see, the merge 
		# step dominates the previous two steps. Because we divide our array
		# into subarrays of size n/2, the recursion tree is essentially a 
		# binary tree. The amount of times we divide the array is equal to the
		# height of the recursion tree, which is log n. Thus, the sort 
		# algorithm runs in O(n log n) time. No additional space is required,
		# however if we factor in the stack frame, then the space complexity is
		# O(log n).



	def get_size(self):
		return self.size


	def __repr__(self):  # Basically traversing the linked list.
		list_sequence = ""
		ptr = self.head

		while (ptr):
			list_sequence += "{} -> ".format(ptr.get_data())
			ptr = ptr.get_next()

		list_sequence += "END\n"

		return list_sequence



linked_list = LinkedList()

print('Inserting 1 at head.')
linked_list.insert_at_head(1)  # 1 -> END
print(linked_list)

print('Inserting 2 at head.')  
linked_list.insert_at_head(2)  # 2 -> 1 -> END
print(linked_list)

print('Inserting 3 at head.')  
linked_list.insert_at_head(3)  # 3 -> 2 -> 1 -> END
print(linked_list)

print('Inserting 6 at tail.')  
linked_list.insert_at_end(6)  # 3 -> 2 -> 1 -> 6 -> END
print(linked_list)

print('Inserting 5 at tail.')
linked_list.insert_at_end(5)  # 3 -> 2 -> 1 -> 6 -> 5 -> END
print(linked_list)

print('Inserting 4 at tail.')
linked_list.insert_at_end(4)  # 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> END
print(linked_list)

print('Size is ' + str(linked_list.get_size()) + '\n')  # Size is 6

print('Sorting list by ascending order.')
linked_list.sort()  # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> END
print(linked_list)




