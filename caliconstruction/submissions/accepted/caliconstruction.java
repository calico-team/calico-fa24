import java.io.*;

class Solution {
    static int solve(String S) {
        boolean is_impossible = false;
        int c_cnt = 0;
        int a_cnt = 0;
        int l_cnt = 0;
        int i_cnt = 0;
        int o_cnt = 0;

        for (char c: S.toCharArray()) {
            switch (c) {
                case 'c':
                case 'u':
                case 'n':
                    c_cnt++;
                    break;
                case 'a':
                    a_cnt++;
                    break;
                case 'l':
                case 'h':
                    l_cnt++;
                    break;
                case 'i':
                    i_cnt++;
                    break;
                case 'o':
                    o_cnt++;
                    break;
                default:
                    is_impossible = true;
                    break;
            }
        }
        if (is_impossible) {
            return -1;
        }
        int ans = Math.max((c_cnt+1)/2, a_cnt);
        ans = Math.max(ans, l_cnt);
        ans = Math.max(ans, i_cnt);
        ans = Math.max(ans, o_cnt);
        return ans;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String S = in.readLine();
            out.println(solve(S));
        }
        out.flush();
    }
}
