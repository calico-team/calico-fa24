import java.io.*;

class Solution {
    /**
     * Return the number of healing items the player needs to use.
     *
     * N: starting health
     * H: amount of healing
     * D: distance out of the storm in meters
     * S: running speed in meters per second
     * P: storm damage per second
     * T: time to heal
     */
    static int solve(int N, int H, int D, int S, int P, int T) {
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
                P = Integer.parseInt(temp[4]),
                T = Integer.parseInt(temp[5]);
            out.println(solve(N, H, D, S, P, T));
        }
        out.flush();
    }
}
