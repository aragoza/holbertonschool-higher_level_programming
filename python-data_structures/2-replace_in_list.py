#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx == None:
        return None
    for i in range(len(my_list)):
        if i == idx:
            my_list[i]=[element]
            return my_list
    return None

if __name__ == "__main__":

    print("{}".format(replace_in_list(my_list, idx, element)))