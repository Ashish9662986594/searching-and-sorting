pos = -1

def search(list, n):

    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list(mid) == n:
            globals() ['pos'] = mid
            return True
        else:
            if list(mid) < n:
                l = mid+1
            else:
                u = mid-1

    return False

list = [3,5,7,8,34,67,90,123]                     # We take a any variable 
n = 67                            # Which data you need to search we put in hear

if search(list, n):
    print("The data is found",pos+1)
else:
    print("The data is not found")