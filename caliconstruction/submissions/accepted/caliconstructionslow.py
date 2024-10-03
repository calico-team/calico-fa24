def solve(S: str) -> int:
    c = 0
    u = 0
    n = 0
    a = 0
    l = 0
    i = 0
    h = 0
    o = 0
    
    for letter in S:
        if letter == "C":
            c += 1
    for letter in S:
        if letter == "U":
            u += 1
    for letter in S:
        if letter == "N":
            n += 1
    for letter in S:
        if letter == "A":
            a += 1
    for letter in S:
        if letter == "L":
            l += 1
    for letter in S:
        if letter == "I":
            i += 1
    for letter in S:
        if letter == "H":
            h += 1
    for letter in S:
        if letter == "O":
            o += 1
    for letter in S:
        if letter != 'C' and letter != 'U' and letter != 'N' and letter != 'A' and letter != 'L' and letter != 'I' and letter != 'H' and letter != 'O':            
            return -1

    c_total = c + u + n
    c_needed = (c_total + 1) // 2
    i_total = i + h

    values = [c_needed, a, l, i_total, o]
    max = 0
    for val in values:
        if val > max:
            max = val
    return max

def main():
    T = int(input())
    for _ in range(T):
        S = input()
        print(solve(S))

if __name__ == '__main__':
    main()
