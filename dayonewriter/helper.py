import math

def list_subset(array: list, size:int =10):
    no_of_elements = len(array)
    subset_len = math.ceil(no_of_elements/size)
    temp = []
    start = 0
    end = size
    for _ in range(subset_len):
        temp.append(array[start:end])
        start +=size
        end = end + size

        if end > no_of_elements:
            end = no_of_elements
    return temp