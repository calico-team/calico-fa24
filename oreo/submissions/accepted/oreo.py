def solve(O: str) -> str:
  '''
  Implements an OREO printer
  O: a string
  '''
  for i in range(len(O)):
    if O[i] == 'O':
      print('[###OREO###]')
    elif O[i] == 'R': # ignore E since its implied E always follows R
      print(' [--------] ')
    elif O[i] == '&':
      print()
  print()


def main():
    T = int(input())
    for _ in range(T):
        S = input()
        solve(S)


if __name__ == '__main__':
    main()
