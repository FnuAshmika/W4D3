# Decorator code to sort the input list

def decorator_insertion_sort(func):
    def inner(self, lst):
        for i in range(1, len(lst)):
            j = i
            while j > 0 and lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                j -= 1
        return func(self, lst)
    return inner

# Code to convert list into linked list
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    @decorator_insertion_sort
    def convert_list(self, lst):
        if not lst:
            return None
        self.head = Node(lst[0]) #Here created the head using element at index 0
        current_node = self.head
        #Now loop through the list to create nodes from remaining elements of list
        for item in lst[1:]:
            current_node.next_node = Node(item)
            current_node = current_node.next_node

        self.print_nodes()

    def print_nodes(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=' -> ')
            current_node = current_node.next_node
        print('None')




a_list = [5,6,3,8,1,4,2,99,20,0]
b_list = ['b','c','a','j','d','f']
linked_list = LinkedList()
linked_list.convert_list(a_list)
linked_list.convert_list(b_list)
    