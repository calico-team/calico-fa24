import java.util.*;

public class Main {
    private static final int[][] DIRS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

	/**
     * Return the maximum number of islands.
     *
     * N: number of rows
     * M: number of columns
     * G: grid of heights
     */
    public static int solve(int N, int M, int[][] G) {
        // Create G' with borders (-1 for always-submerged cells)
        int[][] Gp = new int[N + 2][M + 2];
        for (int[] row : Gp) Arrays.fill(row, -1);
        for (int i = 0; i < N; i++)
            System.arraycopy(G[i], 0, Gp[i + 1], 1, M);

        Map<Integer, List<int[]>> heightMap = new TreeMap<>(Collections.reverseOrder());
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= M; j++)
                heightMap.computeIfAbsent(Gp[i][j], k -> new ArrayList<>()).add(new int[]{i, j});

        DSU dsu = new DSU((N + 2) * (M + 2));
        int maxIslands = 0;
        DSU.islands = 0;
        
        for (Map.Entry<Integer, List<int[]>> entry : heightMap.entrySet()) {
            int h = entry.getKey();
            List<int[]> cells = entry.getValue();
            DSU.islands += cells.size();
            
            for (int[] cell : cells) {
                int i = cell[0], j = cell[1];
                for (int[] d : DIRS) {
                    int ip = i + d[0], jp = j + d[1];
                    if (Gp[ip][jp] >= h)
                        dsu.uni(i * (M + 2) + j, ip * (M + 2) + jp);
                }
            }
            maxIslands = Math.max(maxIslands, DSU.islands);
        }

        return maxIslands;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt(); // Number of test cases
        for (int t = 0; t < T; t++) {
            int N = sc.nextInt(); // Number of rows
            int M = sc.nextInt(); // Number of columns
            int[][] G = new int[N][M];
            
            // Reading the grid
            for (int i = 0; i < N; i++)
                for (int j = 0; j < M; j++)
                    G[i][j] = sc.nextInt();
            
            // Call the solve function and print the result
            System.out.println(solve(N, M, G));
        }
        
        sc.close();
    }
}

class DSU {
    private int[] p, r;
    public static int islands;

    public DSU(int n) {
        p = new int[n];
        r = new int[n];
        for (int i = 0; i < n; i++) p[i] = i;
    }

    public int get(int a) {
        if (a != p[a]) p[a] = get(p[a]);
        return p[a];
    }

    public void uni(int a, int b) {
        a = get(a);
		b = get(b);
        if (a == b) return;
        if (r[b] < r[a]) {
            int temp = a;
            a = b;
            b = temp;
        }
        if (r[b] == r[a]) r[b]++;
        p[a] = b;
        islands--;
    }
}
