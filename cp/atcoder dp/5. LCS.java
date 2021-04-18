import java.util.*;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		String t = sc.nextLine();
		
		int n = s.length(); int m = t.length();
		int[][] dp = new int[n+1][m+1];
		
		for(int i=0; i<n; i++){
			dp[i][0] = 0;
		}
		
		for(int i=0; i<m; i++){
			dp[0][i] = 0;
		}
		
		for(int i=1; i<n+1; i++){
			for(int j=1; j<m+1; j++){
				if(s.charAt(i-1)==t.charAt(j-1)){
					dp[i][j] = dp[i-1][j-1] + 1;
				}
				else{
					dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
				}
			}
		}
		
		int index = dp[n][m];
		char[] result = new char[index+1];
		result[index] = ' ';
		
		int i=n, j=m;
		while(i>0 && j>0){
			if(s.charAt(i-1)==t.charAt(j-1)){
				result[index-1] = s.charAt(i-1);
				i -= 1; j-=1; index-=1;
			}
			else if(dp[i-1][j]>dp[i][j-1]){
				i-=1;
			}
			else{
				j-=1;
			}
		}
		System.out.println(String.valueOf(result));
	}

}
