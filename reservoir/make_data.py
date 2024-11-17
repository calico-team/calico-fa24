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
SEED = '190cmty237csajpdixf,wd'

MX_T = 100
# Assuming max n = max m and max ∑nm = MX_DIM^2
MAIN_MX_DIM, BONUS_MX_DIM = 30, 500
MAIN_MX_G, BONUS_MX_G = 100, 10**9

class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.

    TODO Change this to store the relevant information for your problem.
    """

    def __init__(self, N, M, G):
        self.N = N
        self.M = M
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
        TestCase(6, 5, [
            [18, 2, 19, 2, 10],
            [2, 19, 13, 8, 1],
            [11, 6, 8, 11, 10],
            [8, 14, 6, 12, 9],
            [5, 6, 15, 9, 4],
            [2, 9, 6, 15, 1]
        ]),
        TestCase(5, 7, [
            [1, 1, 1, 2, 5, 1, 1],
            [7, 5, 9, 2, 2, 2, 1],
            [1, 2, 2, 1, 1, 2, 5],
            [1, 2, 5, 1, 5, 2, 1],
            [1, 1, 2, 5, 2, 1, 1],
        ]),
        TestCase(10, 14, [
            [2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 2, 9, 1, 5],
            [2, 1, 1, 3, 1, 1, 3, 1, 1, 1, 2, 5, 9, 6],
            [5, 2, 1, 1, 1, 1, 1, 5, 1, 4, 1, 2, 5, 8],
            [8, 2, 3, 1, 6, 6, 1, 6, 5, 1, 2, 2, 8, 2],
            [6, 9, 1, 1, 6, 5, 1, 6, 6, 5, 1, 1, 2, 2],
            [8, 5, 1, 2, 2, 5, 5, 1, 1, 1, 1, 3, 1, 2],
            [1, 1, 1, 1, 1, 2, 1, 2, 2, 8, 5, 1, 2, 1],
            [1, 4, 2, 8, 1, 1, 1, 2, 9, 5, 9, 1, 8, 6],
            [1, 2, 9, 5, 1, 3, 1, 2, 8, 1, 1, 8, 5, 8],
            [1, 1, 6, 9, 9, 1, 1, 2, 1, 2, 3, 1, 8, 2],
        ])
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
    def make_random_case(n, m, mx_g):
        return TestCase(n, m,
            [[random.randint(0, mx_g) for _ in range(m)] for _ in range(n)]
        )
    
    def make_random_test(mx_dim, mx_g):
        sum_nm = 0
        cases = []
        while True:
            # Generate each case to roughly evenly distribute the total NM
            approx_nm = mx_dim ** 2 // MX_T
            n = int(approx_nm ** 0.5)
            m = approx_nm // n
            if random.random() < 0.5:
                n, m = m, n
            
            sum_nm += n * m
            if len(cases) < MX_T and sum_nm <= mx_dim ** 2:
                cases.append(make_random_case(n, m, mx_g))
            else:
                return cases
    
    # Make test where all grid heights are equal
    def make_uniform_test(n, g):
        return [TestCase(n, n, [[g] * n] * n)]

    main_edge_tests = [
        [TestCase(1, 1, [[42]])], # 1x1
        make_uniform_test(MAIN_MX_DIM, MAIN_MX_G), # max uniform max g
        make_uniform_test(MAIN_MX_DIM, 0), # max uniform 0
        [make_random_case(MAIN_MX_DIM, MAIN_MX_DIM, MAIN_MX_G)] # T = 1 max random
    ]
    for test in main_edge_tests:
        make_secret_test(test, 'main_edge')

    for _ in range(10):
        make_secret_test(
            make_random_test(MAIN_MX_DIM, MAIN_MX_G),
            'main_random'
        )

    bonus_edge_tests = [
        make_uniform_test(BONUS_MX_DIM, BONUS_MX_G), # max uniform max g
        make_uniform_test(BONUS_MX_DIM, 0), # max uniform 0
        [make_random_case(BONUS_MX_DIM, BONUS_MX_DIM, BONUS_MX_G)] # T = 1 max random
    ]
    for test in bonus_edge_tests:
        make_secret_test(test, 'bonus_edge')

    for _ in range(10):
        make_secret_test(
            make_random_test(BONUS_MX_DIM, BONUS_MX_G),
            'bonus_random'
        )


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.

    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    assert 1 <= T <= MX_T
    is_bonus = 'bonus' in file.name
    mx_dim = BONUS_MX_DIM if is_bonus else MAIN_MX_DIM
    mx_g = BONUS_MX_G if is_bonus else MAIN_MX_G
    sum_mn = 0

    for case in cases:
        print(f'{case.N} {case.M}', file=file)
        assert 1 <= case.N <= mx_dim
        assert 1 <= case.M <= mx_dim
        sum_mn += case.N * case.M
        assert sum_mn <= mx_dim ** 2
        # print(case.G, is_bonus)/
        for r in case.G:
            for cell in r:
                assert 0 <= cell <= mx_g

        for row in case.G:
            print(' '.join(list(map(str, row))), file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.

    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.

    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.reservoir_dsu import solve
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
