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

import random, time
from calico_lib import make_sample_test, make_secret_test, make_data
from graph_randomizer import *

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'T1 Keria Fighting!'

class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """


    def __init__(self, N, M, S=None, T=None, edges=None):
        self.N = N
        self.M = M
        if S is None:
            while True:
                S = random.randrange(0, N)
                if S != T:
                    break
        self.S = S
        if T is None:
            while True:
                T = random.randrange(0, N)
                if S != T:
                    break
        self.T = T
        if edges is None:
            self.edges = None
            while not self.are_edges_correct():
                self.edges = self.create_edges()
        else:
            self.edges = edges
        assert self.are_edges_correct()


    def are_edges_correct(self):
        """ Ensure that there is a possible answer given the problem statement conditions """
        if self.edges is None:
            return False
        G = [[] for _ in range(self.N)]
        for e in self.edges:
            G[e[0]].append(e[1])
            G[e[1]].append(e[0])
        
        edgeset = set()
        for e in self.edges:
            u, v = e[0:2]
            if u > v:
                u, v = v, u
            if (u, v) in edgeset:
                return False
            edgeset.add((u, v))

        def dfs(u, t):
            ret = 1
            vis.add(u)
            for v in G[u]:
                if v != t and v not in vis:
                    ret += dfs(v, t)
            return ret

        vis = set()
        if dfs(self.S, self.T) != self.N - 1:
            return False
        vis = set()
        if dfs(self.T, self.S) != self.N - 1:
            return False
        return True


    def create_edges(self):
        graph = GraphRandomizer(range(self.N), self.M)
        edges = graph.edge_set
        edgelist = []
        for e in edges:
            w = random.randint(1, 10 if self.N < 20  else 10000)
            edgelist.append((e[0], e[1], w))
        self.M = len(edgelist)
        return edgelist


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
        TestCase(N=3, M=3, S=0, T=2, edges=[(0,1,1), (1,2,1), (0,2,10)]),
        TestCase(N=4, M=6, S=0, T=3, edges=[(0,1,2), (2,3,2), (0,2,3), (1,3,3), (0,3,10), (1,2,1)]),
        TestCase(N=5, M=6, S=0, T=4, edges=[(0,1,1), (1,2,1), (2,4,1), (0,3,2), (3,4,1), (1,3,2)]),
        TestCase(N=2, M=1, S=0, T=1, edges=[(0,1,20)])
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

    """ Making some simple but exhaustive test cases """
    for _ in range(10):
        main_exhaustive = [TestCase(random.randint(4, 7), random.randint(10, 15)) for _ in range(10)]
        make_secret_test(main_exhaustive, 'main_exhaustive')

    """ Make bigger test cases """
    for _ in range(10):
        main_bigger = [TestCase(random.randint(40, 60), random.randint(150, 200))]
        make_secret_test(main_bigger, 'main_bigger')

    main_edge_cases = [
        TestCase(N=4, M=5, S=0, T=3, edges=[(0,3,1), (0,1,1), (1,2,2), (2,3,1), (1,3,2)]),
        TestCase(N=5, M=6, S=0, T=4, edges=[(0,1,1), (1,2,1), (2,4,1), (1,3,2), (3,4,1), (0,3,3)])
    ]
    make_secret_test(main_edge_cases, 'main_edge')



def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(f'{case.N} {case.M} {case.S} {case.T}', file=file)
        for e in case.edges:
            print(e[0], e[1], e[2], file=file)



def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.

    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    """
    from submissions.time_limit_exceeded.correct import solve as solve_correct
    from submissions.accepted.weighted_matroid import solve as solve_matroid
    from submissions.wrong_answer.mst import solve as solve_wa1
    from submissions.wrong_answer.mst2 import solve as solve_wa2
    from submissions.wrong_answer.mst3 import solve as solve_wa3
    from submissions.wrong_answer.gpt1 import solve as solve_gpt1
    from submissions.wrong_answer.gpt2 import solve as solve_gpt2

    for case in cases:
        # correct_ans = solve_correct(case.N, case.M, case.S, case.T, case.edges)
        start = time.time()
        matroid_ans  = solve_matroid(case.N, case.M, case.S, case.T, case.edges)
        end = time.time()
        print(f'N = {case.N}, M = {case.M}, time = {end - start}, matroid answer = {matroid_ans}')
        # mst1_ans = solve_wa1(case.N, case.M, case.S, case.T, case.edges)
        # mst2_ans = solve_wa2(case.N, case.M, case.S, case.T, case.edges)
        # mst3_ans = solve_wa3(case.N, case.M, case.S, case.T, case.edges)
        # gpt1_ans = solve_gpt1(case.N, case.M, case.S, case.T, case.edges)
        # gpt2_ans = solve_gpt2(case.N, case.M, case.S, case.T, case.edges)
        # assert solve_correct(case.N, case.M, case.S, case.T, case.edges) == solve_matroid(case.N, case.M, case.S, case.T, case.edges)
        print(matroid_ans, file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests,
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
