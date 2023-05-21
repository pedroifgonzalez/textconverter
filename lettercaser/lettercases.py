#!usr/bin/python3
"""
    Module for transformings
    text to different formats using str built-in methods
"""
import string


def to_uppercase(text: str) -> str:
    """Converts to uppercase

    >>> to_uppercase("word")
    'WORD'
    """
    return text.upper()


def to_lowercase(text: str) -> str:
    """Converts to lowercase

    >>> to_lowercase("All Words WERE converted to lower")
    'all words were converted to lower'
    """
    return text.lower()


def to_title_case(text: str) -> str:
    """Converts to title case

    >>> to_title_case("you got a title case")
    'You Got A Title Case'
    """
    return text.title()


def capitalize(text: str) -> str:
    """Capitalize text

    >>> capitalize("initial letter is written in uppercase")
    'Initial letter is written in uppercase'
    """
    return text.capitalize()


def capitalize_after_one_period(text: str) -> str:
    """Capitalize text after every one period

    >>> capitalize_after_one_period("initial letter is written in uppercase after a period too. remember that...")
    'Initial letter is written in uppercase after a period too. Remember that...'

    >>> capitalize_after_one_period("it was dark... I didn't think the light was coming... what a surprise when it did.")
    "It was dark... I didn't think the light was coming... what a surprise when it did."
    """
    count = 0
    output = []
    for pos, char in enumerate(text.lower()):
        char_to_output = char
        if char == ".":
            count += 1
        if char in string.ascii_letters:
            if count == 1 or text[pos] == char.upper():
                char_to_output = char_to_output.upper()
            count = 0
        output.append(char_to_output)

    output[0] = output[0].upper()

    return "".join(output)


def hyphen_case(text: str) -> str:
    """Replace spaces with hyphens

    Args:
        text (str): text target

    Returns:
        str: text modified

    >>> hyphen_case("initial letter is written in uppercase")
    'initial-letter-is-written-in-uppercase'
    """
    return text.replace(" ", "-")


def branch_to_pr(text: str):
    """Convert git branch notation to a more readable PR title

    Args:
        text (str): text target

    >>> branch_to_pr("flex-7/feature")
    'FLEX-7 Feature'
    >>> branch_to_pr("flex-10/feature-important")
    'FLEX-10 Feature important'
    """
    try:
        issue, topic = text.split("/")
        issue = issue.upper()
        topic = topic.capitalize().replace("-", " ")
        return " ".join((issue, topic))
    except ValueError:
        return text


if __name__ == "__main__":
    import doctest

    doctest.testmod()
