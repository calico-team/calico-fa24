import java.io.*;
import java.util.*;

class Solution {
    /**
     * Return the shape displayed by the picture represented by G of dimensions M x N
     *
     * G: a list of strings representing a picture
     * M: integer for number of rows
     * N: integer for number of columns
     */
    static String solve(int M, int N, String[] G) {

        Set<Integer> rowCount = new HashSet<>();
        for (String row : G) {
            int count = 0;
            for (int i = 0; i < N; i++) {
                if (row.charAt(i) == '#') {
                    count++;
                }
            }
            if (count != 0) {
                rowCount.add(count);
            }
        }

        if (rowCount.size() <= 1) {
            return "ferb";
        }
        return "phineas";
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] dimensions = in.readLine().split(" ");
            int M = Integer.parseInt(dimensions[0]), N = Integer.parseInt(dimensions[1]);
            String[] G = new String[M];
            for (int j = 0; j < M; j++) {
                String row = in.readLine();
                G[j] = row;
                }
            out.println(solve(M, N, G));
            }
        out.flush();
        }
    }
