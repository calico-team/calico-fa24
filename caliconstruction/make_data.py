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
import string

from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'caliconstructing this problem'

# TODO
MAX_T = 10
MAX_S = 500

class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """


    def __init__(self, S):
        self.S = S


def make_sample_tests():
    """
    Make all sample test files.
    
    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    
    TODO Write sample tests. Consider creating cases that help build
    understanding of the problem, help with debugging, or possibly help
    identify edge cases.
    """
    main_sample_cases = [
            TestCase('lol'),
            TestCase('coil'),
            TestCase('a'),
            TestCase('unccccc'),
            TestCase('caliconstruction'),
            TestCase('q'),
            TestCase('nonalcoholic')
    ]
    make_sample_test(main_sample_cases, 'main')

def random_string(size, chars):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(size))

def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    
    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """
    case = [TestCase(random_string(10, string.ascii_lowercase)) for _ in range(5)]
    make_secret_test(case, 'main_random')
    case2 = [TestCase('c'*200)]
    make_secret_test(case2, 'main_edge')

    # for i in range(5):
    #     main_random_cases = None
    #     # main_random_cases = [TestCase(random.choice(flat)) for _ in range(max_T)]
    #     make_secret_test(main_random_cases, 'main_random')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    assert 1 <= T <= MAX_T
    for case in cases:
        print(f'{case.S}', file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    # from submissions.accepted.caliconstruction import solve
    # for case in cases:
    #     print(solve(case.S), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
