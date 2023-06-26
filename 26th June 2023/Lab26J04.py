# Check if a Key exists in a dictionary


dictionary = {"a": 1, "b": 2, "c": 3}


def check_present(a):
    return a in dictionary


print(check_present("a"))
print(check_present("z"))


# Remove a key from dictionary

def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary


print(remove_key(dictionary, "b"))

dictionary = {"b": 1, "a": 2, "c": 3}


def sort_my_dict(dictionary):
    return dict(sorted(dictionary.items()))


print(sort_my_dict(dictionary))

# Find the maximum value in a dictionary:

print(max(dictionary.keys()))
print(max(dictionary.values()))