def solve() -> int:
    """
    Perform scan queries to find the length of the shortest path from the vertex
    labeled 1 to the vertex labeled 500 in the graph. Return the length to
    perform the submit query to submit your answer.
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


def main():
    T = int(input())
    for _ in range(T):
        print(f'SUBMIT {solve()}', flush=True)
        response = input()
        if response == 'WRONG_ANSWER':
            exit()


if __name__ == '__main__':
    main()
