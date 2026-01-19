#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[-i-1]))


if __name__ == "__main__":
    print_reversed_list_integer(my_list)