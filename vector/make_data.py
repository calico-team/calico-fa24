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
SEED = 5


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
            TestCase(5, 6, [10, 5, 15, 0, 3],
                     [['FIND'],
                      ['UPDATE', 3, 4, 3],
                      ['FIND'],
                      ['UPDATE', 4, 5, 15],
                      ['UPDATE', 2, 2, 5],
                      ['FIND']])
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
    def make_power_case(n, q, p, fact):
        case = TestCase(n, q, [], [])
        case.N = n 
        case.Q = q
        for i in range(n):
            num = random.randint(4, 15)
            case.arr.append(p ** num * fact)

        cnt = 1
        case.queries.append(['FIND'])
        for i in range(q - 2):
            op = random.randint(0, 2)
            if case.queries[i][0] == 'FIND' or cnt == 2499 or op == 0 or op == 1:
                l = random.randint(1, n)
                r = random.randint(l, n)
                num = random.randint(2, 15)
                case.queries.append(['UPDATE', l, r, p ** num * fact])
            else:
                case.queries.append(['FIND'])
                cnt += 1
        
        case.queries.append(['FIND'])
        cnt += 1
        print(cnt)
        
        return case
    
    def make_random_case(n, q):
        case = TestCase(n, q, [], [])
        case.N = n 
        case.Q = q
        for i in range(n):
            num = random.randint(1, 10**9)
            case.arr.append(num)
        case.queries.append(['FIND'])
        cnt = 1
        for i in range(q - 2):
            op = random.randint(0, 2)
            if case.queries[i][0] == 'FIND' or cnt == 2499 or op == 0 or op == 1:
                l = random.randint(1, n)
                r = random.randint(l, n)
                num = random.randint(1, 10**9)
                case.queries.append(['UPDATE', l, r, num])
            else:
                case.queries.append(['FIND'])
                cnt += 1
        case.queries.append(['FIND'])
        cnt += 1
        print(cnt)
        
        return case
        
    def make_worst_case(n, q):
        case = TestCase(n, q, [], [])
        case.N = n 
        case.Q = q
        for i in range(12):
            case.arr.append(2**29)
        for i in range(29, 0, -1):
            case.arr.append(2**i)
        for i in range(0, 100000 - 42):
            case.arr.append(2)
        case.arr.append(1)
        for i in range(1, 4096, 1):
            for j in range(13):
                if 2**j > i:
                    case.queries.append(['UPDATE', 1, 12 - j + 1, 2**29])
                    break
        for i in range(10000 - 4095 - 5000):
            case.queries.append(['UPDATE', 1, 100000, 0])
        for i in range(2500):
            case.queries.append(['UPDATE', 1, 100000, 0])
            case.queries.append(['FIND'])
        return case


    for i in range(15):
        main_power_cases = [make_power_case(100000, 10000, (i % 2) + 2, 17 if i == 2 else 1)]
        make_secret_test(main_power_cases, 'main_power')
    for i in range(9):
        main_random_cases = [make_random_case(100000, 10000)]
        make_secret_test(main_random_cases, 'main_random')
    for i in range(1):
        main_worst_cases = [make_worst_case(100000, 10000)]
        make_secret_test(main_worst_cases, 'main_worst')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.

    TODO Implement this for your problem.
    """
    assert len(cases) == 1
    for case in cases:
        assert 1 <= case.N <= 10**5
        print(case.N, file=file)
        assert len(case.arr) == case.N 
        assert all(0 <= s <= 10**9 for s in case.arr)
        print(*case.arr, file = file)
        assert 1 <= case.Q <= 10**4
        print(case.Q, file = file)
        if len(case.queries) != case.Q:
            print(len(case.queries), case.Q)
        assert len(case.queries) == case.Q
        cnt = 0
        for q in case.queries:
            if q[0] == 'FIND':
                assert len(q) == 1
                cnt += 1
            else:
                assert q[0] == 'UPDATE'
                assert 1 <= q[1] <= case.N 
                assert q[1] <= q[2] <= case.N
                assert 0 <= q[3] <= 10**9 
                assert len(q) == 4
            print(*q, file = file)
        assert cnt <= 2500

import subprocess
def make_test_out(cases, file, in_filename):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.

    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.

    TODO Implement this for your problem by changing the import below.
    """
    # assert len(cases) == 1
    # from submissions.time_limit_exceeded.faster_brute_force import solve
    # for case in cases:
    #     print(*solve(case.N, case.arr, case.Q, case.queries), file=file, sep='\n')
    myinput = open(in_filename)
    out = subprocess.check_output('./submissions/accepted/a.out', stdin=myinput)
    print(out.decode(), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    subprocess.run(['g++', '-O2', '-o', 'submissions/accepted/a.out', 'submissions/accepted/solution.cpp'])
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
