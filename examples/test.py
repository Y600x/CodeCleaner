# ============================================
# This is a test file for CodeCleaner
# FlashBytes-Team
# ============================================

import os  # operating system module
import sys  # system module


# ----------- Functions ----------------------

def say_hello():  # simple function
    # This function prints hello
    print("Hello")  # inline comment


def add(a, b):
    """
    This function adds two numbers
    """
    return a + b  # return result


# ----------- Classes ------------------------

class TestClass:
    # Class constructor
    def __init__(self, name):
        self.name = name  # assign name

    def greet(self):
        # Greeting method
        print(f"Hello {self.name}")  # print greeting


# ----------- Main ---------------------------

if __name__ == "__main__":

    # Call functions
    say_hello()

    result = add(5, 10)  # calculate sum
    print("Result > ", result)

    user = TestClass("FlashBytes")
    user.greet()


    # Extra blank lines below
