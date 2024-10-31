import java.io.*;

class Solution {
    static void solve(String S) {
        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == 'O') {
                System.out.println("[###OREO###]");
            } 
            else if (S.charAt(i) == 'R') {
                System.out.println(" [--------]");
            }
            else if (S.charAt(i) == '&') {
                System.out.println();
            }
        }
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String S = in.readLine();
            solve(S);
        }
        out.flush();
    }
}
