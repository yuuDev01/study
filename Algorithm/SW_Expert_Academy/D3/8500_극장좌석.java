//https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWz5yIfq74QDFARQ
import java.util.Scanner;
import java.io.FileInputStream;
import java.util.Arrays;

class Solution
{
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T;
        int cnt;
		T=sc.nextInt();
        int[] num;
		for(int test_case = 1; test_case <= T; test_case++)
		{
            cnt = 0;
            int n = sc.nextInt();
            num = new int[n];
            for (int i = 0; i < n ; i++){
				num[i] = sc.nextInt();
               // System.out.println(integer[i]);
            }
            Arrays.sort(num);
            for ( int i = 0; i< n; i++){
                if( i == n-1){
                    cnt += num[i]*2+1;
                }else{
                    cnt += num[i]+1;
                }
            }
           
            System.out.println('#'+String.valueOf(test_case)+' '+cnt);

		}
	}
}