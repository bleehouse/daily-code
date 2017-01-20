public class specialEleven {
	
	public static boolean specialEleven(int n) {
		 int specialEleven = n % 11;
		 return specialEleven == 0 ||specialEleven == 1;  
	}	
	
	public static void main(String[] args) {

		System.out.println(specialEleven(22));
		
	}
}