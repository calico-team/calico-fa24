import java.io.*;

class Solution {
    /**
     * Return the minimum number of sets of CALICO blocks needed to
     * form S, or -1 if it is impossible.
     *
     * S: a string
     */
    static int solve(String S) {
        return 1;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String S = in.readLine();
            out.println(solve(S));
        }
        out.flush();
    }
}
