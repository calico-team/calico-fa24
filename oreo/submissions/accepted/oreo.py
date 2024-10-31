def solve(S: str):
    for i in range(len(O)):
        if S[i] == 'O':
            print('[###OREO###]')
        elif S[i] == 'R': # ignore E since its implied E always follows R
            print(' [--------]')
        elif S[i] == '&':
            print()


def main():
    T = int(input())
    for _ in range(T):
        S = input()
        solve(S)


if __name__ == '__main__':
    main()
