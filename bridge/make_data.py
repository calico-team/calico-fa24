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
SEED = 'uhgynrbtsrenujffvbnljhdsghjgadfghmjkhgfdsacfghjkjhgfvdcrtyiou0o879m,o/po.iuyntrfgbhtyrtybtrybrt4e5eb4y'

max_T_main = 10
max_B_main = 10000
max_N_main = 100
max_Si_main = 100

max_T_bonus = 10
max_B_bonus = 10 ** 18
max_N_bonus = 100_000
max_Si_bonus = 10 ** 13

class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """

    def __init__(self, B, N, S):
        """
        :param B: budget for the bridge
        :param N: number of columns
        :param S: the list of heights
        """
        assert type(B) == int
        assert type(N) == int
        assert type(S) == list
        self.B = B
        self.N = N
        self.S = S


def make_sample_tests():
    """
    Make all sample test files.

    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    """
    main_sample_cases = [
        TestCase(8, 5, [2, 6, 10, 1, 2]),
        TestCase(13, 10, [5, 8, 9, 8, 9, 8, 7, 4, 1, 7]),
        TestCase(44, 12, [9, 21, 4, 31, 10, 20, 31, 28, 16, 29, 9, 11])
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
    def make_random_case(max_length, max_height):
        length = random.randint(1, max_length)
        S = []
        for i in range(length):
            S.append(random.randint(0, max_height))
        B = random.randint(0, sum(S))
        return TestCase(B, length, S)

    # main_edge_cases = [
    #     TestCase(8, 5, [2, 6, 10, 1, 2]),
    #     TestCase(13, 10, [5, 8, 9, 8, 9, 8, 7, 4, 1, 7]),
    #     TestCase(44, 12, [9, 21, 4, 31, 10, 20, 31, 28, 16, 29, 9, 11])
    # ]
    # make_secret_test(main_edge_cases, 'main_edge')

    for i in range(5):
        main_random_cases = [make_random_case(max_N_main, max_Si_main) for _ in range(max_T_main)]
        make_secret_test(main_random_cases, 'main_random')

    for i in range(5):
        bonus_random_cases = [make_random_case(max_N_bonus, max_Si_bonus) for _ in range(max_T_bonus)]
        make_secret_test(bonus_random_cases, 'bonus_random')

    # bonus_edge_cases = [
    #     TestCase(8, 5, [2, 6, 10, 1, 2])

    # ]
    # make_secret_test(bonus_edge_cases, 'bonus_edge')

    # for i in range(5):
    #     bonus_random_cases = [make_random_case(100) for _ in range(100)]
    #     make_secret_test(bonus_random_cases, 'bonus_random')
    pass


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    T = len(cases)

    if 'main' in file.name:
        assert T <= max_T_main
    elif 'bonus' in file.name:
        assert T <= max_T_bonus
    else:
        raise Exception('Invalid file type')
    
    print(T, file=file)
    for case in cases:
        if 'main' in file.name:
            assert case.B <= max_B_main
            assert case.N <= max_N_main
        elif 'bonus' in file.name:
            assert case.B <= max_B_bonus
            assert case.N <= max_N_bonus
        else:
            raise Exception('Invalid file type')

        print(f'{case.B} {case.N}', file=file)

        if 'main' in file.name:
            for Si in case.S:
                assert Si <= max_Si_main
        elif 'bonus' in file.name:
            for Si in case.S:
                assert Si <= max_Si_bonus
        
        print(*case.S, file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.

    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.

    TODO Implement this for your problem by changing the import below.
    """
    # from submissions.accepted.add_arbitrary import solve
    for case in cases:
        print(solve(case.B, case.N, case.S), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
