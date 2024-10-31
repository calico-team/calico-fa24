def solve(S: str):
    cookie = ''
    for i in range(len(S)):
        if S[i] == 'O':
            print('[###OREO###]')
            cookie += '[###OREO###]\n'
        elif S[i] == 'R': # ignore E since its implied E always follows R
            print(' [--------]')
            cookie += ' [--------]\n'
        elif S[i] == '&':
            print()
            cookie += '\n'
    return cookie


def main():
    T = int(input())
    for _ in range(T):
        S = input()
        return solve(S)


if __name__ == '__main__':
    main()
