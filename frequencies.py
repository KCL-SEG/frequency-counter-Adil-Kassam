"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    if len(items) == 0:
        return frequencies
    else:
        for i in range(len(items)):
            item = str(items[i])
            frequencies[item] = frequencies.get(item, 0) + 1



        return frequencies
