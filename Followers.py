def display_friends(friends):
    for username, followers in friends.items():
        print(username + ":", followers, "followers")


friends = {
    "Bhide": "2.3K",
    "Jethalal": "5.1K",
    "Champaklal": "1.8K"
}

display_friends(friends)
