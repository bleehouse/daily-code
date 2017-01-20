public class specialEleven {
	public static boolean getSpecialEleven(int n) {
		 int specialEleven = n % 11;
		 return specialEleven == 0 ||specialEleven == 1;  
	}	
	
	public static void main(String[] args) {
    	System.out.println(getSpecialEleven(22));
	}
}