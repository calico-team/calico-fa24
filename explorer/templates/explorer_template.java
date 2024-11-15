import java.io.*;

class Solution {
    /**
     * Perform scan queries to find the length of the shortest path from the
     * vertex labeled 1 to the vertex labeled 500 in the graph. Return the
     * length to perform the submit query to submit your answer.
     */
    static int solve() throws IOException {
        // YOUR CODE HERE
        return 0;
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

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            out.println("SUBMIT " + solve());
            out.flush();
            String response = in.readLine();
            if (response.equals("WRONG_ANSWER")) {
                System.exit(0);
            }
        }
    }
}
