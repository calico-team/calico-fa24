def solve() -> None:
    """
    Perform scan queries and a submit query to find the length of the shortest
    path from the vertex labeled 1 to the vertex labeled 1000 in the graph.
    """
    # YOUR CODE HERE


def scan(v: int) -> int:
    """
    Scan at the vertex labeled v. Returns the label of a random vertex that v is
    connected to.
    """
    print(f'SCAN {v}', flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()
    return int(response)


def submit(d: int) -> str:
    """
    Submit your guess for the length of the shortest path. Returns CORRECT if
    your guess is correct and exits if your guess is wrong.
    """
    print(f'SUBMIT {d}', flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()
    return response


def main():
    T = int(input())
    for _ in range(T):
        solve()
    verdict = input()


if __name__ == '__main__':
    main()
