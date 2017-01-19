// CodingBat Logic-1 > sortaSum  
// http://codingbat.com/

public class SortaSumExam {

	public static int sortaSum(int a, int b) {
		  int sum = a + b;

		  if (sum > 9 && sum < 20) {
		    sum = 20;
		  }
		  
		  return sum;
	}	
	
	public static void main(String[] args) {
		System.out.println(sortaSum(3, 4));
		System.out.println(sortaSum(9, 4));
		System.out.println(sortaSum(10, 11));
	}

}
