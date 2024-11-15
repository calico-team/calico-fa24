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
    
    queue = collections.deque([1])
    dist = {1: 0}
    while True:
        curr_vertex = queue.popleft()
        for adj in cache_scan(curr_vertex):
            if adj == N:
                submit(dist[curr_vertex] + 1)
                return
            if adj not in dist:
                dist[adj] = dist[curr_vertex] + 1
                queue.append(adj)


def scan(v: int) -> int:
    print(f'SCAN {v}', flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()
    return int(response)


def submit(d: int) -> str:
    print(f'SUBMIT {d}', flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()
    return response


def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == '__main__':
    main()
