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
SEED = 1


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.

    TODO Change this to store the relevant information for your problem.
    """


    def __init__(self, N, Q, arr, queries):
        self.N = N
        self.Q = Q
        self.arr = arr
        self.queries = queries


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
        TestCase(5, 1, [2, 2, 2, 2, 2], [[2]])
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
    def make_random_case(n, q):
        case = TestCase(n, q, [], [])
        case.N = n 
        case.Q = q
        for i in range(n):
            num = random.randint(0, 10)
            case.arr.append(2 ** num)

        case.queries.append([2])
        for i in range(q - 1):
            op = random.randint(0, 1)
            if case.queries[i][0] == 2 or op == 0:
                l = random.randint(1, n)
                r = random.randint(l, n)
                num = random.randint(0, 10)
                case.queries.append([1, l, r, 2 ** num])
            else:
                case.queries.append([2])
        
        return case

    for i in range(10):
        main_random_cases = [make_random_case(100, 100)]
        make_secret_test(main_random_cases, 'main_random')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.

    TODO Implement this for your problem.
    """
    assert len(cases) == 1
    for case in cases:
        print(case.N, file=file)
        print(*case.arr, file = file)
        print(case.Q, file = file)
        for q in case.queries:
            print(*q, file = file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.

    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.

    TODO Implement this for your problem by changing the import below.
    """
    assert len(cases) == 1
    from submissions.brute_force import solve
    for case in cases:
        print(*solve(case.N, case.arr, case.Q, case.queries), file=file, sep='\n')


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
