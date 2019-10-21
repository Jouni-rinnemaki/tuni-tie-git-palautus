
def debug_print(debug_msg=None, **kwargs):

    if debug_msg:
        print(debug_msg)

    for key, value in kwargs.items():
        print("{}: {}".format(key, value))


if __name__ == "__main__":
    input_str = input("Enter numbers, separated by ',': ")

    input_list = input_str.split(",")
    debug_print(input_list=input_list)

    value_list = []
    for x in input_list:
        try:
            value_list.append(int(x))
        except ValueError as err:
            print("Invalid input.")
            quit(1)

    debug_print(value_list=value_list)
