"""

Write a function that returns the number of users in a chatroom based on the following rules:

    If there is no one, return "no one online".
    If there is 1 person, return "user1 online".
    If there are 2 people, return "user1 and user2 online".
    If there are n>2 people, return the first two names and add "and n-2 more online".

"""

def chatroom_status(users):
    n = len(users)
    if n == 0:
        return "no one online"
    elif n == 1:
        #return users[0] + " online"
        return "{} online".format(users[0])
    elif n == 2:
        return "{} and {} online".format(users[0],users[1])
    elif n > 2:
        return "{}, {} and {} more online".format(users[0],users[1],str(n-2))