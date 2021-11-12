package programmers.step1.java;

import java.util.Arrays;

public class GCDandLCM {
	public static void main(String args[]) {	
		int n1= 3, m1 =12;
		int n2= 2, m2 =5;
			
		System.out.println(Arrays.toString(solution(n1,m1)));
		System.out.println(Arrays.toString(solution(n2,m2)));
		
	}
	
    public static int[] solution(int n, int m) {
        int gcd=0, lcm = 0;
        int mx = Math.max(n,m);
        int mn = Math.min(n,m);
        while(true){
        	int extra = mx % mn;
        	if(extra == 0){//나머지가 0이면 
        		lcm = mn;//최대공약수
        		break;
        	}
        	mx = mn;
        	mn = extra; 	
        }
        gcd = n*m / lcm;
        int[] answer = {lcm, gcd,};
        return answer;
    }
}
