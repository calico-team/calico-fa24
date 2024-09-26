def solve(S: str) -> int:
    c_count = 0
    a_count = 0
    l_count = 0
    i_count = 0
    o_count = 0  

    for c in S:
        match c:
            case 'c':
                c_count += 1
            case 'u':
                c_count += 1
            case 'n':
                c_count += 1
            case 'a':
                a_count += 1
            case 'l':
                l_count += 1
            case 'i':
                i_count += 1
            case 'h':
                i_count += 1
            case 'o':
                o_count += 1

    if (c_count + a_count + l_count + i_count + o_count != len(S)):
            return -1
    else:  
        return max((c_count + 1) // 2, a_count, l_count, i_count, o_count)

def main():
    T = int(input())
    for _ in range(T):
        S = input()
        print(solve(S))


if __name__ == '__main__':
    main()
