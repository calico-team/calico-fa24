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
SEED = '039qgj0a9fa09wf9a2'

MAIN_MX_T, MAIN_MX_VAL = 100, 100
BONUS_1_MX_T, BONUS_1_MX_VAL = 10**5, 10**9


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.

    TODO Change this to store the relevant information for your problem.
    """


    def __init__(self, N, H, D, S, P, L):
        # Checks that the inputs are valid (allows the player to survive)
        if not N > (D // S) * P:
            assert H > P * L
            assert N > P * L

        self.N = N
        self.H = H
        self.D = D
        self.S = S
        self.P = P
        self.L = L


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
        TestCase(10, 3, 12, 4, 2, 0),
        TestCase(5, 3, 12, 4, 2, 0),
        TestCase(3, 3, 12, 4, 2, 0),
        TestCase(4, 2, 1, 1, 3, 0)
    ]
    make_sample_test(main_sample_cases, 'main')

    bonus_sample_cases = [
        TestCase(883459283, 694224901, 355732753, 426, 19123, 36292)
    ]
    make_sample_test(bonus_sample_cases, 'bonus')


def make_secret_tests():
    """
    Make all secret test files.

    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.

    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """
    def make_random_case(max_val, is_main):
        def ceildiv(a, b):
            return -(a // -b)
        
        N = random.randint(1, max_val)
        H = random.randint(1, max_val)
        D = random.randint(1, max_val)
        S = random.randint(1, max_val)
        # Upper bounds P so that a valid nonzero L is likely to exist
        P = random.randint(1, min(N, H))
        if is_main:
            L = 0
        else:
            # In this case (numerator < 0), the player can run without heals
            # So no further restrictions on P and L are needed
            if N > (D // S) * P:
                if random.random() < 0.5:
                    L = random.randint(0, max_val)
                # Makes it likely to have some cases with premax answer < 0 (denominator > 0)
                # Need H > PL still
                else:
                    L = random.randint(0, ceildiv(H, P) - 1)
            # Otherwise, we need to make sure H > PL and N > PL
            else:
                L = random.randint(0, ceildiv(min(N, H), P) - 1)
        # print(N, H, D, S, P, L, 'num =', ((D // S) * P) - N, 'den =', H - (P * L))
        return TestCase(N, H, D, S, P, L)

    main_edge_cases = [
        TestCase(100, 100, 99, 100, 100, 100), # ans = 0
        TestCase(1, 1, 100, 1, 100, 0) # ans = 10^4
    ]
    make_secret_test(main_edge_cases, 'main_edge')

    for _ in range(10):
        main_random_cases = [
            make_random_case(MAIN_MX_VAL, True)
            for _ in range(MAIN_MX_T)
        ]
        make_secret_test(main_random_cases, 'main_random')

    bonus_edge_cases = [
        TestCase(10 ** 9, 10 ** 9, 10 ** 9 - 1, 10 ** 9, 10 ** 9, 10 ** 9), # ans = 0
        TestCase(1, 1, 10 ** 9, 1, 10 ** 9, 0) # ans = 10^18
    ]
    make_secret_test(bonus_edge_cases, 'bonus_edge')

    for _ in range(10):
        bonus_random_cases = [
            make_random_case(BONUS_1_MX_VAL, False)
            for _ in range(BONUS_1_MX_T)
        ]
        make_secret_test(bonus_random_cases, 'bonus_random')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.

    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(f'{case.N} {case.H} {case.D} {case.S} {case.P} {case.L}', file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.

    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.

    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.fortnite_math import solve
    for case in cases:
        print(solve(case.N, case.H, case.D, case.S, case.P, case.L), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
