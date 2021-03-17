"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        
        i = 1
        current = self.head  
        if position < 1:
            return None      
        while i <= position: 
            if i == position: 
                return current
            current = current.next
            i += 1 
        return None
            
            
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        
        i = 1
        current = self.head
        if position > 1:
            while i < position:
                if i == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next               
                i += 1     
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
                
                
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value:
            previous = current
            current = current.next
        if current.value == value: 
            if previous:
                previous.next = current.next
            else: 
                self.head = current.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)


# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)

''' A slightly differente way of making Linked Lists'''

class node: 
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class linked_list: 
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        
    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total
    
    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)
        
    def get(self, index):
        if index >= self.length():
            print('ERROR: "GET" index out of range.')
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: 
                return cur_node.data
            else:
                cur_idx += 1
                
    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' index out of range.")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1
        

my_list = linked_list()
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

print("Element at second index: {}".format(my_list.get(2)))

my_list.erase(1)

my_list.display()