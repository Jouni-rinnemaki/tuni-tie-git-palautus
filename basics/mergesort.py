
def debug_print(debug_msg=None, **kwargs):

    if debug_msg:
        print(debug_msg)

    for key, value in kwargs.items():
        print("{}: {}".format(key, value))


if __name__ == "__main__":
    input_str = input("Enter numbers, separated by ',': ")

    unsorted_list = input_str.split(",")

    debug_print(unsorted_list=unsorted_list)
