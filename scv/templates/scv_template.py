def solve(R: int, C: int, S: str) -> str:
    """
    Return the shape of displayed by ASCII string S of dimensions R x C
    
    S: a string representing an ASCII picture
    R: integer for number of rows
    C: integer for number of columns
    """
    # YOUR CODE HERE
    return 0


def main():
    T = int(input())
    for _ in range(T):
        temp= input().split()
        S = input()
        R, C = int(temp[0]), int(temp[1])
        print(solve(R, C, S))

if __name__ == '__main__':
    main()
