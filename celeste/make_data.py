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
from sys import stdout
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

    def add_edge_wall(self):
        for r in self.G:
            r.append("#")
            r.insert(0, "#")
        self.N += 2
        self.M += 2
        self.G.insert(0, ["#"]*self.M)
        self.G.append(["#"]*self.M)
        return self

    def test_in(self, file):
        print(f'{self.N} {self.M} {self.K}', file=file)
        for row in self.G:
            print(''.join(row), file=file)


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
            TestCase(3, 9, 5, [
                list('#########'),
                list('#S...E..#'),
                list('#########'),
                ]),
            TestCase(8, 13, 10, [
                list('#############'),
                list('#.####*....*#'),
                list('#.####.####.#'),
                list('#S....*.....#'),
                list('#.####.######'),
                list('#.####.######'),
                list('#.#........E#'),
                list('#############'),
                ]),
            TestCase(4, 5, 2, [
                list('#####'),
                list('#S.##'),
                list('#.#E#'),
                list('#####'),
                ]),
            TestCase(5, 9, 6, [
                list('#########'),
                list('#*......#'),
                list('#S#####.#'),
                list('##E.....#'),
                list('#########'),
                ]),
            TestCase(5, 9, 6, [
                list('#########'),
                list('#.*.....#'),
                list('##S####.#'),
                list('###E....#'),
                list('#########'),
                ]),
            ]
    make_sample_test(main_sample_cases, 'main')

    # bonus_sample_cases = [
    # ]
    # make_sample_test(bonus_sample_cases, 'bonus')

randi = random.randint
def pure_random(n: int, m: int, crystal_cnt: int, wall_cnt: int, max_k = None):
    g = [['.']*m for _ in range(n)]
    for _ in range(crystal_cnt):
        g[randi(0, n-1)][randi(0, m-1)] = '*'
    for _ in range(wall_cnt):
        g[randi(0, n-1)][randi(0, m-1)] = '#'
    g[randi(0, n-1)][randi(0, m-1)] = 'S'
    g[randi(0, n-1)][randi(0, m-1)] = 'E'
    if max_k == None:
        max_k = max(n, m)
    return TestCase(n, m, randi(2, max(n, m)), g).add_edge_wall()

def line_random(n: int, m: int, crystal_cnt: int, max_k = None):
    g = [['.']*m for _ in range(n)]
    for i in range(0, n, 2):
        g[i] = ['#'] * m
        g[i][randi(0, m-1)] = '.'
    for _ in range(crystal_cnt):
        g[randi(0, n-1)][randi(0, m-1)] = '*'
    g[0][randi(0, m-1)] = 'S'
    g[n-1][randi(0, m-1)] = 'E'
    if max_k == None:
        max_k = max(n, m)
    return TestCase(n, m, randi(2, max(n, m)), g).add_edge_wall()

def gen(max_k, subproblem):
    basic_rand = [pure_random(10, 10, 10, 10, max_k) for _ in range(10)]
    make_secret_test(basic_rand, subproblem + '_basic')
    basic_rand = [line_random(10, 10, 10, max_k) for _ in range(10)]
    make_secret_test(basic_rand, subproblem + '_basic')

    c = int(5e4)
    basic_rand = [pure_random(100, 1800, c, c, max_k) for _ in range(1)]
    make_secret_test(basic_rand, subproblem + '_edge')
    basic_rand = [line_random(100, 1800, c, max_k) for _ in range(1)]
    make_secret_test(basic_rand, subproblem + '_edge')
    basic_rand = [line_random(1800, 100, c, max_k) for _ in range(1)]
    make_secret_test(basic_rand, subproblem + '_edge')

def make_secret_tests():
    """
    Make all secret test files.

    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.

    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """

    # TODO: impossible case

    gen(5, 'main')
    gen(None, 'bonus')


def make_test_in(cases: list[TestCase], file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.

    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        assert case.is_valid()
        case.test_in(file)


import subprocess
import resource
def make_test_out(cases, file, in_filename):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.

    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.

    TODO Implement this for your problem by changing the import below.
    """

    myinput = open(in_filename)
    out = subprocess.check_output('./bin.out', stdin=myinput)
    print(out.decode(), file=file)

    # print(out)
    # from submissions.accepted.add_arbitrary import solve
    # for case in cases:
        # print(solve(case.A, case.B), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    subprocess.run(['g++', '-O2', '-Wl,-z,stack-size=268435456', '-o', 'bin.out', 'submissions/accepted/celeste.cpp'])
    resource.setrlimit(resource.RLIMIT_STACK, (268435456, 268435456))
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
