import collections

N = 500
D = 3

def solve() -> None:
    adj_cache = [set() for _ in range(N + 1)]
    def cache_scan(v):
        while len(adj_cache[v]) < D:
            w = scan(v)
            adj_cache[v].add(w)
            adj_cache[w].add(v)
        return adj_cache[v]
    
    queue_from_1 = collections.deque([1])
    queue_from_n = collections.deque([N])
    
    visited_from_1 = {1}
    visited_from_n = {N}

    dist_guess = 0
    
    while True:
        dist_guess += 1
        if len(queue_from_1) <= len(queue_from_n):
            for _ in range(len(queue_from_1)):
                curr_vertex = queue_from_1.popleft()
                for adj in cache_scan(curr_vertex):
                    if adj not in visited_from_1:
                        visited_from_1.add(adj)
                        queue_from_1.append(adj)
                        if adj in visited_from_n:
                            return dist_estimate
        else:
            for _ in range(len(queue_from_n)):
                curr_vertex = queue_from_n.popleft()
                for adj in cache_scan(curr_vertex):
                    if adj not in visited_from_n:
                        visited_from_n.add(adj)
                        queue_from_n.append(adj)
                        if adj in visited_from_1:
                            return dist_estimate


def scan(v: int) -> int:
    print(f'SCAN {v}', flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()
    return int(response)


def main():
    T = int(input())
    for _ in range(T):
        print(f'SUBMIT {solve()}', flush=True)
        response = input()
        if response == 'WRONG_ANSWER':
            exit()


if __name__ == '__main__':
    main()
