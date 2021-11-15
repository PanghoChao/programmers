package programmers.step1.java;

import java.util.Arrays;

public class Remove_smallest {
	public static void main(String args[]) {	
		int[] arr1= {4,3,2,1};
		int[] arr2= {10};
			
		System.out.println(Arrays.toString(solution(arr1)));
		System.out.println(Arrays.toString(solution(arr2)));
		
	}
	
    public static int[] solution(int[] arr) {
    	if(arr.length == 1) {
    		int[] nothing = {-1};
    		return nothing;
    	}
        int mn= 2147483647;
        for(int e : arr) {
        	 mn = Math.min(e, mn);
        }

        int j = 0;
        int[] answer = new int[arr.length - 1];
        for(int e: arr) {
        	
        	if(e == mn) {
        		continue;
        	}
        	answer[j] = e;
        	++j;
    	}
    
        return answer;
    }
}
