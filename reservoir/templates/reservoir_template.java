import java.util.Scanner;

class Solution {
    /**
     * Return the maximum number of islands.
     *
     * N: number of rows
     * M: number of columns
     * G: grid of heights
     */
    public static int solve(int N, int M, int[][] G) {
        return 0;
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
