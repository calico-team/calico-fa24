import java.io.*;

class Solution {
    /**
     * Return the shape of displayed by ASCII string S of dimensions R x C
     *
     * S: a string representing an ASCII picture
     * R: integer for number of rows
     * C: integer for number of columns
     */
    static String solve(int M, int N, String[] G) {
        // YOUR CODE HERE
        return "";
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
