#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""

import json
import requests


def count_words(subreddit, word_list, after="", count=None):
    """Function to count_words
    """
    if count is None:
        count = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in data['data']['children']:
            for word in topic['data']['title'].split():
                clean_word = ''.join(char for char in word if char.isalnum()).lower()
                if clean_word in word_list:
                    if clean_word not in count:
                        count[clean_word] = 1
                    else:
                        count[clean_word] += 1

        after = data['data']['after']
        if after is None:
            print_results(count)
        else:
            count_words(subreddit, word_list, after, count)


def print_results(count):
    sorted_counts = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print("{}: {}".format(word, count))


# Example usage:
count_words('unpopular', ['you', 'unpopular', 'vote', 'down', 'downvote', 'her', 'politics'])
