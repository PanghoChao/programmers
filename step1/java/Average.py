public class Average {
	public static void main(String[] args) {
		int[] arr1 = {1,2,3,4};
		int[] arr2 = {5,5};
		System.out.println(solution(arr1));	
		System.out.print(solution(arr2));	
	}

    public static double solution(int[] arr) {
        double answer = 0;
        for(int e : arr){
            answer += e;    
        }
        answer= answer/arr.length;
        return answer;

    }
}
