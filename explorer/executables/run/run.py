import random

def run():
    log(f'Begin interaction')
    
    GOAL = int(input_test_in())
    
    T = int(input_test_in())
    print_prog(T)
    
    total_scan_queries = 0
    
    for case in range(1, T + 1):
        log(f'Begin test case #{case} of {T}')
        
        N = int(input_test_in())
        ANSWER = int(input_test_in())
        
        adj_list = [None, *(list(map(int, input_test_in().split())) for _ in range(N))]
        
        while True:
            query_str = input_prog()
            query_args = query_str.strip().upper().split()
            if len(query_args) != 2:
                give_WA(f'Invalid query format: "{query_str}"')
            
            type, arg = query_args
            if type == 'SCAN':
                if not arg.isdigit():
                    give_WA(f'Invalid argument for SCAN: "{arg}"')
                    
                arg = int(arg)
                if not (1 <= arg <= N):
                    give_WA(f'SCAN argument out of range: "{arg}"')
                
                scan(arg, adj_list)
                total_scan_queries += 1
                
            elif type == 'SUBMIT':
                if not arg.isdigit():
                    give_WA(f'Invalid argument for SUBMIT: "{arg}"')
                
                arg = int(arg)
                submit(arg, ANSWER)
                
            else:
                give_WA(f'Invalid query type: "{type}"')
            
            if type == 'SUBMIT':
                break
    
    if total_scan_queries > GOAL * N:
        give_WA(f'Too many queries. Average should be no more than {GOAL} but was {total_scan_queries / N}.')
    
    log('End interaction')
    give_AC()

def scan(arg, adj_list):
    print_prog(random.choice(adj_list[arg]))

def submit(arg, ANSWER):
    if arg == ANSWER:
        print_prog('CORRECT')
    else:
        print_prog('WRONG_ANSWER')
        give_WA(f'Wrong answer. Expected {ANSWER} but got {arg} instead.')

################################################################################

import io
import sys

_log = []
_test_in, _prog_out = None, None

def main():
    if len(sys.argv) != 3:
        _print_err('Incorrect number of arguments')
        exit(1)
    
    _log_without_tabs('Judge:\tUser:\tInfo:')
    
    _, test_in_path, prog_out_path = sys.argv
    with open(test_in_path, 'r') as test_in:
        with open(prog_out_path, 'w') as prog_out:
            global _test_in, _prog_out
            _test_in, _prog_out = test_in, prog_out
            run()

def give_AC():
    try:
        temp = ''
        while not temp:
            temp = input().strip()
        give_WA(f'Unexpected trailing output when judge was finished: {temp}')
    except EOFError:
        pass
    
    _print_prog_out('AC')
    exit(0)

def give_WA(reason):
    log('End of log')
    
    _print_prog_out('WA')
    _print_prog_out('Reason:', reason)
    _print_prog_out('Interaction Log:')
    for line in _log:
        _print_prog_out(line)
    
    try:
        print('WRONG_ANSWER', flush=True)
    except BrokenPipeError as e:
        pass
    
    _exhaust_input_prog()
    exit(0)

def give_IE(reason):
    log('End of log')
    
    _print_err('Run executable internal error:', reason)
    
    _print_prog_out('IE')
    _print_prog_out('Run executable internal error:', reason)
    _print_prog_out('Interaction Log:')
    for line in _log:
        _print_prog_out(line)
    
    _exhaust_input_prog()
    exit(1)

def input_test_in():
    try:
        return _test_in.readline().strip()
    except EOFError:
        give_IE('End of test input while judge expected more input')

def input_prog():
    try:
        prog_output = input()
        _log_without_tabs(f'\t{prog_output}')
        return prog_output
    except (EOFError, BrokenPipeError): # TODO check if BrokenPipeError is necessary
        give_WA('User program exited early when judge expected more output')

def _exhaust_input_prog():
    try:
        while True:
            input()
    except:
        pass

def print_prog(*args, **kwargs):
    prog_input = io.StringIO()
    print(*args, **kwargs, file=prog_input, end='')
    try:
        print(*args, **kwargs, flush=True)
        _log_without_tabs(prog_input.getvalue())
    except BrokenPipeError:
        temp = prog_input.getvalue()
        give_WA(f'User program exited early when judge had more output: {temp}')

def _print_prog_out(*args, **kwargs):
    print(*args, **kwargs, file=_prog_out)

def _print_err(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

def log(message):
    _log_without_tabs(f'\t\t{message}')

def _log_without_tabs(message):
    if len(message) > 100:
        message = message[:100] + ' (truncated after 50 bytes)'
    _log.append(message)

if __name__ == '__main__':
    main()

