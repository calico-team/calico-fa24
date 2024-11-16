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

max_T = 100
max_N_M = int(2e5 - 5)
max_N = int(2e5 - 5)

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


    def is_valid(self, is_basic = False):
        assert (3 <= self.N <= max_N)
        assert (3 <= self.M <= max_N)
        assert (self.M * self.N <= max_N_M)
        assert len(self.G) == self.N
        for i in range(self.N):
            assert len(self.G[i]) == self.M
        s_cnt = e_cnt = 0
        for i in range(self.N):
            for j in range(self.M):
                if self.G[i][j] == 'S':
                    s_cnt += 1
                if self.G[i][j] == 'E':
                    e_cnt += 1
                assert self.G[i][j] in "#.*SE"
        assert s_cnt == 1 and e_cnt == 1
        assert 2<=self.K<=max_N
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
def pure_random(n: int, m: int, crystal_cnt: int, wall_cnt: int, k: int = 2):
    g = [['.']*m for _ in range(n)]
    for _ in range(crystal_cnt):
        g[randi(0, n-1)][randi(0, m-1)] = '*'
    for _ in range(wall_cnt):
        g[randi(0, n-1)][randi(0, m-1)] = '#'
    g[randi(0, 1)][randi(0, min(m-1, 50))] = 'S'
    g[randi(2, n-1)][randi(max(m-30, 0), m-1)] = 'E'
    return TestCase(n, m, k, g).add_edge_wall()

def line_random(n: int, m: int, crystal_cnt: int, k: int = 2):
    g = [['.']*m for _ in range(n)]
    for i in range(1, n, 2):
        g[i] = ['#'] * m
        g[i][randi(0, m-1)] = '.'
    for _ in range(crystal_cnt):
        g[randi(0, n-1)][randi(0, m-1)] = '*'
    g[0][randi(0, min(m-1, 50))] = 'S'
    g[n-1][randi(max(m-30, 0), m-1)] = 'E'
    return TestCase(n, m, k, g).add_edge_wall()

def gen(max_k: int, subproblem):
    # 12 * 12 * 100
    basic_rand = [line_random(8, 8, randi(2, 100), randi(2, max_k)) for _ in range(max_T)]
    make_secret_test(basic_rand, subproblem + '_basic_line')
    for _ in range(6):
        basic_rand = [pure_random(8, 8, randi(2, 200), randi(2, 200), randi(2, max_k)) for _ in range(max_T)]
        make_secret_test(basic_rand, subproblem + '_basic')
        # basic_rand = [pure_random(4, 4, randi(2, 20), randi(2, 20), randi(2, max_k)) for _ in range(max_T)]
        # make_secret_test(basic_rand, subproblem + '_tiny_rand')

    c1 = int(5e2)
    c2 = int(1e4)
    for _ in range(2):
        x1 = randi(c1, c2)
        x2 = randi(c1, c2)
        x3 = randi(min(max_k-2, int(1e3)), max_k)
        basic_rand = [pure_random(100, 1800, x1, x2, x3) for _ in range(1)]
        make_secret_test(basic_rand, subproblem + '_edge')
        basic_rand = [line_random(100, 1800, x1, x3) for _ in range(1)]
        make_secret_test(basic_rand, subproblem + '_edge')
        basic_rand = [line_random(1800, 100, x1, x3) for _ in range(1)]
        make_secret_test(basic_rand, subproblem + '_edge')
        basic_rand = [pure_random(3, int(4e4-100), x1, x2, x3) for _ in range(1)]
        make_secret_test(basic_rand, subproblem + '_thin')
        basic_rand = [line_random(3, int(4e4-100), x1, x3) for _ in range(1)]
        make_secret_test(basic_rand, subproblem + '_thin_line')

    c1 = int(50)
    c2 = int(1000)
    for _ in range(4):
        x1 = randi(c1, c2)
        x2 = randi(c1, c2)
        x3 = randi(min(max_k-2, int(1e3)), max_k)
        basic_rand = [pure_random(100, 1800, x1, x2, x3) for _ in range(1)]
        make_secret_test(basic_rand, subproblem + '_sparse')
        basic_rand = [line_random(100, 1800, x1, x3) for _ in range(1)]
        make_secret_test(basic_rand, subproblem + '_sparse')
        # 6 * 3e4 = 18e5
        basic_rand = [pure_random(3, int(4e4-100), x1, x2, min(max_k, int(1e4))) for _ in range(1)]
        make_secret_test(basic_rand, subproblem + '_thin_sparse')
        basic_rand = [line_random(3, int(4e4-100), x1, min(max_k, int(1e4))) for _ in range(1)]
        make_secret_test(basic_rand, subproblem + '_thin_line_sparse')

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
    gen(max_N, 'bonus')


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
    print(out.decode(), file=file, end='')

    # print(out)
    # from submissions.accepted.add_arbitrary import solve
    # for case in cases:
        # print(solve(case.A, case.B), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    subprocess.run(['g++', '-O2', '-Wl,-z,stack-size=268435456', '-o', 'bin.out', 'submissions/accepted/nacho.cpp'])
    resource.setrlimit(resource.RLIMIT_STACK, (268435456, 268435456))
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
