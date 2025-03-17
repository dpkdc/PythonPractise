#
# n= int(input("Enter a number: "))
# fac=1
# for num in range(1,n+1):
#     fac*=num
# print(fac)
from collections import defaultdict

# data = "hello"
# ascii_dict={}
# for char in data:
#     ascii_dict={char:ord(char)}
#     print(ascii_dict)

# User watch history
user_watch_history = {
    "john_doe": ["John Wick", "Mad Max"],
    "alice": ["Forrest Gump", "The Shawshank Redemption"],
}

# Recommendation system based on watched content
recommendations = {
    "John Wick": ["The Equalizer", "Nobody"],
    "Mad Max": ["Fury Road", "Edge of Tomorrow"],
    "Forrest Gump": ["Cast Away", "The Green Mile"],
}


def get_recommendations(username):
    watched_mov= user_watch_history.get(username,[])
    suggested=set()

    for muv in watched_mov:
        suggested.update(recommendations.get(muv,[]))

    return list(suggested) if suggested else "No recommendation"

print(get_recommendations("ruby"))