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

import networkx as nx

N = 1000
D = 3
EASY_GOAL = 1400
HARD_GOAL = 250

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = '''Delicious in Dungeon (Japanese: ダンジョン飯, Hepburn: Danjon Meshi, lit. "Dungeon Meal") is a Japanese manga series written and illustrated by Ryoko Kui. It was serialized in Enterbrain's seinen manga magazine Harta from February 2014 to September 2023, with its chapters collected in fourteen tankōbon volumes. The story follows a group of adventurers in a fantasy world who, after failing to defeat a dragon that consumed one of their own, embark on a journey through a dungeon to revive her, surviving by cooking and eating the monsters they encounter along the way.'''


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """

    def __init__(self, graph):
        self.graph = graph


def make_dungeon_graph():
    graph = None
    while not graph or not nx.is_connected(graph):
        graph = nx.random_regular_graph(D, N)
    return graph


def make_sample_tests():
    """
    Make all sample test files.

    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    """
    sample_cases = [TestCase(make_dungeon_graph()) for _ in range(1000)]
    
    # main and sample are intended to be the same
    make_sample_test(sample_cases, 'main')
    make_sample_test(sample_cases, 'bonus')


def make_secret_tests():
    """
    Make all secret test files.

    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    """
    for i in range(9):
        secret_cases = [TestCase(make_dungeon_graph()) for _ in range(1000)]
        
        # main and sample are intended to be the same
        make_secret_test(secret_cases, 'main')
        make_secret_test(secret_cases, 'bonus')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    assert 'main' in file.name or 'bonus' in file.name
    if 'main' in file.name:
        print(EASY_GOAL, file=file)
    else:
        print(HARD_GOAL, file=file)
    
    T = len(cases)
    assert T == 1000
    print(T, file=file)
    
    for case in cases:
        assert set(case.graph.nodes) == set(range(1000))
        assert nx.is_connected(case.graph)
        
        for i in range(1000):
            neighbors = [n + 1 for n in case.graph.neighbors(i)]
            assert len(neighbors) == 3
            assert all(1 <= n <= 1000 for n in neighbors)
            
            print(*neighbors, file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.

    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    """
    for case in cases:
        answer = nx.shortest_path_length(case.graph, 0, 999)
        print(answer, file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
