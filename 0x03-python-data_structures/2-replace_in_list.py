#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list)-1:
        print(my_list)
        return None
    else:
        my_list[idx] = element
        for i in range(0, len(my_list)):
            print("{:d}".format(my_list[i]))
