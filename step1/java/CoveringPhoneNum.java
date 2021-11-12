package programmers.step1.java;


public class CoveringPhoneNum {
	public static void main(String[] args) {
		String phone_number	= "01033334444"	;
		String phone_number2 = "027778888";
		System.out.println(solution(phone_number));	
		System.out.print(solution(phone_number2));	
	}

    public static String solution(String phone_number) {
    		String answer = new String(new char[phone_number.length() - 4]).replace("\0", "*");
    		
    	
    		String num4 = phone_number.substring(phone_number.length()-4);
	        answer += num4;
	        return answer;
    }
}

