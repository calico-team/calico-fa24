import java.io.*;

class Solution {
    /**
     * Return the sum of A and B.
     *
     * A: a non-negative integer
     * B: another non-negative integer
     */
    static void solve(String S) {
        // YOUR CODE HERE
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            String S = temp[0];
            solve(S);
        }
        out.flush();
    }
}
