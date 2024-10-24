MX_N = 10**5
seen_slopes = set()
x, y = 1, 1
houses = []
for _ in range(MX_N):
    while y / x in seen_slopes:
        if y == 1:
            x, y = 1, x + 1
        else:
            x += 1
            y -= 1
    seen_slopes.add(y / x)
    houses.append((x, y))

def solve(N: int) -> list[int]:
    """
    Return a tuple containing the coordinates X and Y.

    N: a positive integer, the address of your house
    """
    return houses[N - 1]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(*solve(N))


if __name__ == "__main__":
    main()
