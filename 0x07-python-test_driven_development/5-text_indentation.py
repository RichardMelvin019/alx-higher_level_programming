#!/usr/bin/python3
"""

This module contains a function that indents texts

"""


def text_indentation(text):
    '''This function prints a text with 2 new lines after each ".", "?", or ":"

    Args:
        text (str): The string to be printed

    Raises:
        TypeError: If text is not a string

    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count_1 = 0
    while count_1 < len(text) and text[count_1] == " ":
        count_1 = count_1 + 1

    while count_1 < len(text):
        print(text[count_1], end="")
        if text[count_1] == "\n" or text[count_1] in ".?:":
            if text[count_1] in ".?:":
                print("\n")
            count_1 = count_1 + 1
            while count_1 < len(text) and text[count_1] == " ":
                count_1 = count_1 + 1
            continue
        count_1 = count_1 + 1
