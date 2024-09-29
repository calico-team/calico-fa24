def solve(S: str) -> int:
    c_count = 0
    a_count = 0
    l_count = 0
    i_count = 0
    o_count = 0  

    for c in S:
        match c:
            case 'C':
                c_count += 1
            case 'U':
                c_count += 1
            case 'N':
                c_count += 1
            case 'A':
                a_count += 1
            case 'L':
                l_count += 1
            case 'I':
                i_count += 1
            case 'H':
                i_count += 1
            case 'O':
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
