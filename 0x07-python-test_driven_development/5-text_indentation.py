#!/usr/bin/python3
""" Function that prints a text with 2 new lines after specific chars """


def text_indentation(text):
    """
    Prints a new text with 2 new lines after: '.', '?' & ':'

    Args:
        text (str): String of chars

    Raises:
        TypeError: If 'text' is not a string
    """   
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    new_text = text.strip()
    result = ""

    for ch in new_text:
        result += ch
        if (ch == '.' or ch == '?' or ch == ':'):
            print(result.strip())
            print()
            result = ""
    print(result.strip(), end="")