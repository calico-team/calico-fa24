import java.io.*;

class Solution {
    /**
     * Return the shortest time for you to escape the storm.
     *
     * N: starting health
     * H: healing per second
     * D: distance out of the storm in meters
     * S: running speed in meters per second
     * P: storm damage per second
     */
    static double solve(double N, double H, double D, double S, double P) {
        double time_to_escape = D / S;
        double damage_taken_to_escape = P * time_to_escape;
        if (damage_taken_to_escape > N) {
            if (P >= H) {
                return -1.0;
            }
            double extra_health_needed = damage_taken_to_escape - N;
            double time_to_heal = extra_health_needed / (H - P);
            time_to_escape += time_to_heal;
        }
        return time_to_escape;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            long N = Integer.parseInt(temp[0]),
                H = Integer.parseInt(temp[1]),
                D = Integer.parseInt(temp[2]),
                S = Integer.parseInt(temp[3]),
                P = Integer.parseInt(temp[4]);
            out.println(solve(N, H, D, S, P));
        }
        out.flush();
    }
}
