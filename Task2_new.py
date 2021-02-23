import json


def read_file(file):
    """
    Reads file and return information in needed format.
    """
    file = open(file, "r", encoding="utf-8")
    data = json.load(file)
    if type(data) == dict:
        data = [data]
    return data


def check_additional_data(value):
    """
    Function for checking the type of the object and getting deep information from file.
    """
    if type(value) == str or type(value) == int:
        print(f"Value by the key you've chosen: {value}")
    elif type(value) == dict:
        keys = list(value.keys())
        print(f"There are such keys: {keys}")
        user_key = input("Choose one: ")
        if user_key in keys:
            val = value[user_key]
            print(f"The value by the key you've chosen: {val}")
            check_additional_data(val)
    elif type(value) == list:
        long = len(value)
        print(f"The value has {long} elements")
        user_digit = input(f"Choose one from range 0 - {long - 1} : ")
        if int(user_digit) in range(long):
            element = value[int(user_digit)]
            if type(element) == dict:
                keys_2 = list(element.keys())
                print(f"There are such keys: {keys_2}")
                inp_user = input("Choose one: ")
                if inp_user in keys_2:
                    print(f"The value by the key you've chosen: {element[inp_user]}")
                else:
                    print("Incorrect key")
        else:
            print("Incorrect digit")


def get_main_data(file):
    """
    Main function for getting information from file.
    """
    data = read_file(file)
    lst_keys = []

    for dictionary in data:
        keys = list(dictionary.keys())
        lst_keys.append(keys)
    long = len(lst_keys)
    print(f"There are {long} dictionaries in this file")
    number = input("Choose one: ")

    if int(number) in range(long):
        main_dict = data[int(number)]
        main_keys = list(main_dict.keys())
        print(f"There are such keys: {main_keys}")
        choice = input("Choose one: ")

        if choice in main_keys:
            value = main_dict[choice]
            check_additional_data(value)
        else:
            print("Incorrect key")
            get_main_data(file)
    else:
        get_main_data(file)
        print("Incorrect number")
