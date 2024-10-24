import java.io.*;

class Solution {
    /**
     * Print out an Oreo
     *
     * S: a string
     */
    static void solve(String S) {
        // YOUR CODE HERE
        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == 'O') {
                System.out.println("[---OREO---]");
            } 
            else if (S.charAt(i) == 'R') {
                System.out.println(" [########] ");
            }
            else if (S.charAt(i) == '&') {
                System.out.println();
            }
        }
        System.out.println();
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
