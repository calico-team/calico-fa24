import java.io.*;

class Solution {
    /**
     * Return the minimum time needed for you to exit the storm.
     * 
     * N: starting health
     * H: healing per second
     * D: distance out of the storm in meters
     * S: running speed in meters per second
     * P: storm damage per second
     */
    static long solve(long N, long H, long D, long S, long P) {
        // YOUR CODE HERE
        return -1;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]),
                H = Integer.parseInt(temp[1]),
                D = Integer.parseInt(temp[2]),
                S = Integer.parseInt(temp[3]),
                P = Integer.parseInt(temp[4]);
            out.println(solve(N, H, D, S, P));
        }
        out.flush();
    }
}
