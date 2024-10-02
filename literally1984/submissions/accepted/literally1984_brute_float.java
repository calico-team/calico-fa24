import java.io.*;
import java.util.*;

class Solution {
    static List<Integer> solve(int N) {
        Set<Double> seenSlopes = new HashSet<>();
        int x = 1, y = 1;
        
        for (int address = 0; address < N;) {
            double slope = (double) x / y;
            if (!seenSlopes.contains(slope)) {
                address++;
                seenSlopes.add(slope);
            }
            
            if (address == N) {
                break;
            }
            
            if (y == 1) {
                y = x + 1;
                x = 1;
            } else {
                x++;
                y--;
            }
        }
        
        return Arrays.asList(x, y);
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
