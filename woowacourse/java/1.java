// 연습해보기
// 
// java code
public class WoowaTech1 {
	 public static void main(String args[]){
		 String intArrayAsString = Arrays.toString(returnArrayInt(args));
		 System.out.println("Returned Integer Array: " + intArrayAsString);
		 
		 
	 }
	 static int[] returnArrayInt(String args[]) {
		 int cnt1= 0, cnt2= 0, cnt3 = 0;
		 
		 for(int i = 0;i < args.length ; i++) {
			 
			 if(args[i] == "1") {
				 cnt1 ++;
			}else if(args[i] == "2") {
				cnt2++;
			}else {
				cnt3++;
			}
			 		 
		 }
		 int mx = Math.max(cnt3 ,Math.max(cnt1 ,cnt2));
		 
		 
		 return new int[]{mx - cnt1, mx - cnt2, mx - cnt3};
        
    }
	 
	 
