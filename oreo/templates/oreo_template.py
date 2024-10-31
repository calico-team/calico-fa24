def solve(S: str):
    """
    Print one line for each token in S to draw the cookie.

    S: cookie name
    
    """
    # YOUR CODE HERE


def main():
    T = int(input())
    for _ in range(T):
        S = input()
        solve(S)

if __name__ == '__main__':
    main()
