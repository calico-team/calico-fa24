#!/usr/bin/env python
"""
Make test data for the problem.

To set up this script, do the following:
    - Set the seed to be something different, long, and arbitrary.
    - Set up the TestCase class to hold relevant information for your problem.
    - Write sample and secret tests in their respective functions.
    - Write input and output code in their respective functions.
Everything else will be handled by the make_data function in calico_lib.py.

You can also run this file with the -v argument to see debug prints.
"""

import random
from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'OREOHJIQWBNWJFHRJWERFJIWHFNJ'

def solve(S: str):
    cookie = ''
    for i in range(len(S)):
        if S[i] == 'O':
            cookie += '[###OREO###]\n'
        elif S[i] == 'R': # ignore E since its implied E always follows R
            cookie += ' [--------]\n'
        elif S[i] == '&':
            cookie += '\n'
    return cookie

class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """

    def __init__(self, S):
        self.S = S


def make_sample_tests():
    """
    Make all sample test files.

    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    """
    main_sample_cases = [
        TestCase("OREO"),
        TestCase("O&REO"),
        TestCase("O&O"),
        TestCase("OREOREO"),
        TestCase("RERERERE"),
        TestCase("OOOO"),
        TestCase("OREOO"),
        TestCase("OREOREREREORE")
    ]
    make_sample_test(main_sample_cases, 'main')


def make_secret_tests():
    """
    Make all secret test files.

    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.

    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """
    def make_random_case(max_length):
        def random_token(n):
            t = ["O", "RE", "&"]
            first = random.randint(0, 1)
            return t[first] + ''.join(random.choices(t, k=n-1))
        N = random.randint(0, max_length)
        return TestCase(random_token(N))
    
    for i in range(5):
        main_random_cases = [make_random_case(100) for _ in range(100)]
        make_secret_test(main_random_cases, 'main_random')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(f'{case.S}', file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.

    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    """
    for case in cases:
        print(solve(case.S), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
