"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""


def anagrams(word, words):
    result_list = list()
    word_set = set(word)
    for w in words:
        if word_set == set(w) and len(word) == len(w):
            result_list.append(w)
    return result_list


print(anagrams('abba', ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba',
                        'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa']))

"""
Other Solutions

1.
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]

2.
from collections import Counter

def anagrams(word, words):
    counts = Counter(word)
    return [w for w in words if Counter(w) == counts]
"""
