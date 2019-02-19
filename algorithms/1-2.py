def easy_search(list, item):

    count_easy_search = 0

    for index in range(len(list)):
        count_easy_search+=1

        if list[index] == item:
            print ('count_easy_search = %d'%count_easy_search)
            return index

    return None

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    count_binary_search = 0

    while low <= high:
        count_binary_search += 1

        mid = (low + high) / 2
        if list[mid] == item:
            print ("count_binary_search = %d"%count_binary_search)
            return mid
        if list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

print easy_search(my_list, 36)
print easy_search(my_list, -1)

print

print  binary_search(my_list, 36)
print  binary_search(my_list, -1)

print ("Hello World!")