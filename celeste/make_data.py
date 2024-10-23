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
SEED = 'flying strawberry'

max_T = 10
max_N_M = 2e5 - 10
max_N = 2e5 - 10

class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.

    Celeste:
    go from top left to bottom right, dash distance: K
    in make test out we surround it with walls
    """

    def __init__(self, N: int, M: int, K: int, G: list[list[str]]):
        self.N = N
        self.M = M
        self.K = K
        self.G = G

    def is_valid(self):
        if not (1 <= self.N <= max_N):
            return False
        if not (1 <= self.M <= max_N):
            return False
        if not (self.M * self.N <= max_N_M):
            return False
        if len(self.G) != self.N:
            return False
        for i in range(self.N):
            if len(self.G[i]) != self.M:
                return False
        for i in range(self.N):
            for j in range(self.M):
                if self.G[i][j] not in "#.*SE":
                    return False
        return True

    def make_out(self):
        print(self.N, self.M, self.K)
        for row in self.G:
            for c in row:
                print(c, end='')
            print()

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
    ]
    make_sample_test(main_sample_cases, 'main')

    bonus_sample_cases = [
    ]
    make_sample_test(bonus_sample_cases, 'bonus')

randi = random.randint
def pure_random(n: int, m: int, crystal_cnt: int, wall_cnt: int):
    g = [['.']*m for _ in range(n)]
    for _ in range(crystal_cnt):
        g[randi(0, n-1)][randi(0, m-1)] = '*'
    for _ in range(wall_cnt):
        g[randi(0, n-1)][randi(0, m-1)] = '#'
    g[randi(0, n-1)][randi(0, m-1)] = 'S'
    g[randi(0, n-1)][randi(0, m-1)] = 'E'
    return TestCase(n, m, randi(2, max(n, m)), g)

def line_random(n: int, m: int, crystal_cnt: int):
    g = [['.']*m for _ in range(n)]
    for _ in range(crystal_cnt):
        g[randi(0, n-1)][randi(0, m-1)] = '*'
    g[randi(0, n-1)][randi(0, m-1)] = 'S'
    g[randi(0, n-1)][randi(0, m-1)] = 'E'
    return TestCase(n, m, randi(2, max(n, m)), g)

def make_secret_tests():
    """
    Make all secret test files.

    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.

    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """

    main_edge_cases = [
    ]
    make_secret_test(main_edge_cases, 'main_edge')

    bonus_edge_cases = [
    ]
    make_secret_test(bonus_edge_cases, 'bonus_edge')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.

    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(f'{case.A} {case.B}', file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.

    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.

    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.add_arbitrary import solve
    for case in cases:
        print(solve(case.A, case.B), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
