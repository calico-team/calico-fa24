import java.io.*;

class Solution {
    /**
     * Perform scan queries and a submit query to find the length of the
     * shortest path from the vertex labeled 1 to the vertex labeled 1000 in the
     * graph.
     */
    static void solve() throws IOException {
        // YOUR CODE HERE
    }
    
    /**
     * Scan at the vertex labeled v. Returns the label of a random vertex that v
     * is connected to.
     */
    static int scan(int v) throws IOException {
        out.println("SCAN " + v);
        out.flush();
        String response = in.readLine();
        if (response.equals("WRONG_ANSWER")) {
            System.exit(0);
        }
        return Integer.parseInt(response);
    }
    
    /**
     * Submit your guess for the length of the shortest path. Returns CORRECT if
     * your guess is correct and exits if your guess is wrong.
     */
    static String submit(int d) throws IOException {
        out.println("SUBMIT " + d);
        out.flush();
        String response = in.readLine();
        if (response.equals("WRONG_ANSWER")) {
            System.exit(0);
        }
        return response;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            solve();
        }
    }
}
