import java.io.*;
import java.util.*;

class Solution {
    /**
     * Return a length 2 List containing the coordinates X and Y.
     * 
     * N: a positive integer, the address of your house
     */
    static List<Integer> solve(int N) {
        // YOUR CODE HERE
        
        return Arrays.asList(-1, -1);
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]);
            List<Integer> ans = solve(N);
            out.println(ans.get(0) + " " + ans.get(1));
        }
        out.flush();
    }
}
