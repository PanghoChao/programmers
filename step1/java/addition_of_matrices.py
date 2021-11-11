package org.opentutorails.javatutorials.array;

import java.util.Arrays;

public class Array_CodingTest {
	public static void main(String[] args) {
		int[][] arr1 = {{1,2} , {3, 4}};
		int[][] arr2 = {{3,4} , {5, 6}};
		System.out.print(Arrays.deepToString(solution(arr1,arr2)));	
	}

    public static int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr1[0].length];
        for(int i = 0 ; i< arr1.length; i++){
            for(int j =0; j<arr1[i].length; j++){
                answer[i][j] = arr1[i][j]+arr2[i][j];
            }
        }
        return answer;
	}
}

