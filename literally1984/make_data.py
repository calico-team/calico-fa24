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
SEED = "aodgoipjsdasdijofioajsdf"

MAIN_MX_T, MAIN_MX_N = 100, 100
BONUS_1_MX_T, BONUS_1_MX_N = 10**5, 10**5
BONUS_2_MX_T, BONUS_2_MX_N = 10**5, 10**9

class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """

    def __init__(self, N: int):
        self.N = N


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
        TestCase(1),
        TestCase(2),
        TestCase(3),
        TestCase(5),
        TestCase(14),
        TestCase(22),
        TestCase(37),
        TestCase(61),
    ]
    make_sample_test(main_sample_cases, "main")

    bonus_2_sample_cases = [
        TestCase(123456789),
        TestCase(10**9),
    ]
    make_sample_test(bonus_2_sample_cases, "bonus2")


def make_secret_tests():
    """
    Make all secret test files.

    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.

    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """
    def make_random_cases(mn_N, mx_N, T):
        return [TestCase(random.randint(mn_N, mx_N + 1)) for _ in range(T)]

    # Main
    make_secret_test(
        make_random_cases(1, MAIN_MX_N, random.randint(2, MAIN_MX_T)),
        "main_random"
    )
    assert MAIN_MX_N <= MAIN_MX_T, "Can't make a complete main test file"
    make_secret_test(
        [TestCase(i) for i in range(1, MAIN_MX_N + 1)],
        "main_complete"
    )

    # Bonus 1
    make_secret_test(
        make_random_cases(1, BONUS_1_MX_N, random.randint(2, BONUS_1_MX_T)),
        "bonus_1_random"
    )
    assert BONUS_1_MX_N <= BONUS_1_MX_T, "Can't make a complete bonus 1 test file"
    make_secret_test(
        [TestCase(i) for i in range(1, BONUS_1_MX_N + 1)],
        "bonus_1_complete"
    )

    # Bonus 2
    make_secret_test(
        make_random_cases(1, BONUS_2_MX_N, random.randint(2, BONUS_2_MX_T)),
        "bonus_2_random"
    )
    make_secret_test(
        make_random_cases(1, BONUS_2_MX_N, BONUS_2_MX_T),
        "bonus_2_max_random"
    )
    make_secret_test(
        [TestCase(BONUS_2_MX_N - i) for i in range(BONUS_2_MX_T)],
        "bonus_2_max_large"
    )


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.

    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(f"{case.N}", file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.

    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.

    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.binsearch import solve

    for case in cases:
        print(*solve(case.N), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, make_test_in, make_test_out, SEED)


if __name__ == "__main__":
    main()
