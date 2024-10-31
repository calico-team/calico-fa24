import java.io.*;

class Solution {
    /**
     * Print one line for each token in S to draw the cookie.
     *
     * S: cookie name
     */
    static void solve(String S) {
        // YOUR CODE HERE
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String S = in.readLine();
            solve(S);
        }
        out.flush();
    }
}
