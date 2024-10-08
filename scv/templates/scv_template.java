import java.io.*;

class Solution {
    /**
     * Return the shape of displayed by ASCII string S of dimensions R x C
     *
     * S: a string representing an ASCII picture
     * R: integer for number of rows
     * C: integer for number of columns
     */
    static String solve(int R, int C, String S) {
        // YOUR CODE HERE
        return -1;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            String S = in.readLine();
            int A = Integer.parseInt(temp[0]), B = Integer.parseInt(temp[1]);
            out.println(solve(A, B, S));
        }
        out.flush();
    }
}
