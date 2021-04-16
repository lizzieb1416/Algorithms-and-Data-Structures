

def bubbleSort(A):
    # A is a list of sortable items

    has_swap = True
    
    while has_swap:
        has_swap = False
        
        for j in range(len(A) - 1): 
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                has_swap = True

my_list = [19, 13, 6, 2, 18, 8]

bubbleSort(my_list)
print(my_list)