#!/usr/bin/python3

def element_at(my_list, idx):
    if idx == None:
        return None
    for i in my_list:
        if i == idx:
            my_list[i] = []
            return my_list
    return None

if __name__ == "__main__":

    print("{}".format(element_at(my_list, idx)))
