# Strings
# Regular strings
"I recommend using double-quoted strings,"
"so you don't have to use backslash (\)"
"to escape apostrophes (')."

'This string won\'t work without a backslash.'

"""Docstrings,
strings that are surround by three pairs of quotes,
allow you to write across multiple lines.
"""

(
    "You can also put multiple strings "
    "inside of parentheses and "
    "Python will put them together for you!"
)

# Use f-strings to insert code into strings
my_var = [1, 2, 3]
f"The value of my_var is {my_var}."

# Names
# Variable names should be written in snake_case
my_var = [1, 2, 3]
my_var = "Variables can change"

def my_func():
    """Function names should also be snake_case."""

# Constants, variables that we don't plan on modifying,
# should be written in SCREAMING_SNAKE_CASE
ALWAYS_FIVE = 5

# kebab-case works only in strings, not variable names
my_str = "kebab-case"

# Assign three variables in a row
x = y = z = 3

# Create a string
my_str = "a few words in a string"

# Combine two methods in a horizontal method chain
mystr.split().index("words")

# Wrap with parentheses to chain methods vertically
(mystr
 .split()
 .index("words")
)

# Create a word list
word_list = my_str.split()

# Replace the first word with !
mylist[0] = "!"
mylist

# For loops
# When to write for loop:
# 1. Not creating a Python object (creating a file)
# 2. When you are translating math into code (e.g. summation using +=)

for i in range(1, 9):
    print(i)
    y *= i
    print(y)

for huzzah in range(4):
    print(huzzah <= 1)

import pathlib

for i in range(9):
    pathlib.Path(
        f"test{i}.txt"
    ).write_text(
        f"This is file {i}."
    )

# Functions
# When to write a function:
# 1. Always!
# 2. Whenever you might need to reuse code
# 3. When you want to abstract away complex code
# 4. When you want to document your code (be a good human being)

# Define a function called word_count
def word_count(string: str):
    """Count the words in a string.

    Arguments:
        string: A string that contains words.

    Returns:
        int: The number of words in the input string.

    """
    word_list = string.split()
    return len(word_list)

print(word_count.__doc__)
print(word_count.__annotations__)
help(word_count)

# Define a function called triple
def triple(x: int):
    # Python ignores comments entirely
    """Docstrings get stored in the __doc__ attribute."""
    return x*3

# Access the information on the triple function
print(triple.__doc__)
print(triple.__annotations__)
help(triple)

def triple(x: int):
    """Multiply a number by three."""
    return x * 3

# If a function has a docstring,
# it can be defined without a code block
def triple(x: int):
    # Python ignores comments entirely
    """Functions without return statements return None."""

# Access the information on the triple function
print(triple.__doc__)
help(triple)

# Access the information on the triple function

# Define a function called average
from typing import List

def average(x: List[float]) -> float:
    """Average a list of numbers.

    The mean (average) of a series of numbers is
    the sum of the series divided by the
    the length of the series.

    Arguments:
        x: An iterable containing numbers.

    Returns:
        The mean of input values.
    """
    return sum(x) / len(x)

# Define a function called median
def median(x: List[float]) -> float:
    """Return the median.

    The median is the middle value
    if the length of x is odd or
    the average of the two middle values
    if the length of x is even.

    Arguments:
        x: An iterable containing numbers.

    Returns:
        The middle value or average of middle values.
    """
    sorted_series = sorted(x)
    series_length = len(x)
    middle_index = series_length // 2
    middle_value = sorted_series[middle_index]
    if series_length % 2 != 0:
        return middle_value
    else:
        return (middle_value + sorted_series[middle_index - 1]) / 2
