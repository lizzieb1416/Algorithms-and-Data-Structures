

# Lists pass by reference
list1 = [1, 2, 3]

list2 = list1
list2.append(4)

print(list1)
print(list2)

# To pass a list by value I have to copy it 
list_a = ['a', 'b', 'c']

list_b = list_a.copy()
list_b.append('d')

print(list_a)
print(list_b)

# Variables with data values pass by value. There is no need to make a copy to pass it by value
A = "The value of A"

B = A
B = "The value of B"

print(A)
print(B)

