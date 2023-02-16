# Decorator code to sort the input list

def decorator_insertion_sort(func):        # USING INSERTION SORT
    def inner(*args):
        lst = args[1]
        for i in range(1, len(lst)):
            j = i
            while j > 0 and lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                j -= 1
        return func(*args)
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
        
        self.get_list()

    def get_list(self):
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

#################################################### ANOTHER APPROACH #################################################
    
def decorator_bubble_sort(func):        # USING BUBBLE SORT
    def inner(lst):
        n = len(lst)
        for i in range(n):
            is_swap = False
            for j in range(n-1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    is_swap = True
            n -= 1
            if is_swap == False:
                break
        return func(lst)
    return inner

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

@decorator_bubble_sort
def linked_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current_node = head
    for item in lst[1:]:
        current_node.next_node = Node(item)
        current_node = current_node.next_node
    current_node.next_node = None
    return head

def show_list(head):
    current_node = head
    while current_node:
        print(current_node.value, end=' -> ')
        current_node = current_node.next_node
    print('None')

c_list = [5,299,3,8,1,4,2,99,20,0]
d_list = ['b','z','a','e','d','f']

show_list(linked_list(c_list))
show_list(linked_list(d_list))