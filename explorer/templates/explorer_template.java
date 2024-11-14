import java.io.*;

class Solution {
    /**
     * TODO
     */
    static int scan(int v) throws IOException {
        out.println("SCAN " + v);
        out.flush();
        return Integer.parseInt(in.readLine());
    }

    /**
     * TODO
     */
    static int solve() throws IOException {
        return 0;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int result = solve();
            out.println("SUBMIT " + result);
            out.flush();
        }
    }
}
