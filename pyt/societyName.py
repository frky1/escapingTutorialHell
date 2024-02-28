"""

A group of friends have decided to start a secret society. The name will be the first letter of each of their names,

sorted in alphabetical order.

Create a function that takes in a list of names and returns the name of the secret society.

"""


def society_name(friends):
    lst = []
    for friend in friends:
        lst += friend[0]

    sorted_lst = sorted(lst)

    return ''.join(sorted_lst)