#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx == None:
        return my_list
    elif idx <= len(my_list) and idx >= 0:
        new_list = my_list
        new_list[idx] = element
        return new_list
    else:
        return my_list


if __name__ == "__main__":
    print("{}".format(new_in_list(my_list, idx, element)))
