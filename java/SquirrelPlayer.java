// CodingBat Logic-1 > squirrelPlay  
// http://codingbat.com/

public class SquirrelPlayer {

	public static boolean squirrelPlay(int temp, boolean isSummer) {
		  int upperLimit = 90;
		  boolean isSquirrelsPlay = false;
		  if (isSummer == true) {
		    upperLimit = 100;
		  }
		  
		  if (temp >= 60 && temp <= upperLimit) {
		    isSquirrelsPlay = true;
		  }
		  
		  return isSquirrelsPlay;
		}	
	
	public static void main(String[] args) {
		System.out.println();
		System.out.println(squirrelPlay(70, false));
		System.out.println(squirrelPlay(95, false));
		System.out.println(squirrelPlay(95, true));
	}

}
