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
import scv_generate
from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 9833719837291

class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """

    def __init__(self, N, M, G):
        self.M = M
        self.N = N
        self.G = G

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
        TestCase(5, 5, ['.....', '.....', '..#..', '..##.', '.....']),
        TestCase(5, 5, ['#####', '#####', '#####', '#####', '#####']),
        TestCase(3, 5, ['###..', '.##..', '..#..']),
        TestCase(8, 20, ['....................', '....................', '....................', '....................', 
                         '....................', '####################', '####################', '####################']),
        TestCase(2, 2, ['##', '#.']),
        TestCase(5, 5, ['####.', '.###.', '..##.', '...#.', '.....'])
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
    def make_random_case():
        triangle_or_square = random.randint(0, 1)
        N = random.randint(4, 100)
        M = random.randint(4, 100)
        if triangle_or_square == 0:
            G = scv_generate.generate_triangle(N, M)
        else:
            G = scv_generate.generate_square(N, M)
        return TestCase(N, M, G)
    
    for _ in range(10):
        main_random_cases = [make_random_case() for _ in range(100)]
        make_secret_test(main_random_cases, 'main_random')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(f'{case.N} {case.M}', file=file)
        for i in range(len(case.G)):
            print(case.G[i], file=file)

def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.scv import solve
    for case in cases:
        print(solve(case.N, case.M, case.G), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
