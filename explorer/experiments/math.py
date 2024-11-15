import pandas as pd
import numpy as np
import pyperclip as pc

import experiments_v2

D = 3
N = 500

wikip_data = experiments_v2.test_solve_func(experiments_v2.solve_wikipedia_bfs, 1000)
early_data = experiments_v2.test_solve_func(experiments_v2.solve_early_return_bfs, 1000)
unopt_data = experiments_v2.test_solve_func(experiments_v2.solve_unoptimized_bidirectional_bfs, 1000)
picky_data = experiments_v2.test_solve_func(experiments_v2.solve_picky_bidirectional_bfs, 1000)

dict = {'wikip': wikip_data, 'early': early_data, 'unopt': unopt_data, 'picky': picky_data}

df = pd.DataFrame(dict)

wikip_means = [df['wikip'].sample(500).mean() for _ in range(1000)]
early_means = [df['early'].sample(500).mean() for _ in range(1000)]
unopt_means = [df['unopt'].sample(500).mean() for _ in range(1000)]
picky_means = [df['picky'].sample(500).mean() for _ in range(1000)]

def get_stats(queries_list):
    print('mean', np.mean(queries_list))
    print('std', np.std(queries_list))
    print('median', np.median(queries_list))
    
    pc.copy(f'histogram({queries_list}, {N // 10})')
    print('desmos histogram copied to clipboard')
