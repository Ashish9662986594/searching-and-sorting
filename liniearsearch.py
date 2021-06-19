def search(list, n):                       # the search function is not inbuilt so we crete the function
    i = 0

    while i< len(list):                    # With help of len you scan the  all data   
        if list[i] == n:                   # When the i == n then return the value
            return True
        i = i + 1
    return False
        


list = [5,8,4,6,9,2]                     # We take a any variable 
n = 10                                   # Which data you need to search we put in hear

if search(list, n):
    print("The data is found")
else:
    print("The data is not found")
