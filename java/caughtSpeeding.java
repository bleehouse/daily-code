// CodingBat Logic-1 > caughtSpeeding   
// http://codingbat.com/

public class caughtSpeeding  {

    public int caughtSpeeding(int speed, boolean isBirthday) {
        if (isBirthday == true) {
            speed = speed - 5;
        }
        
        int result = 0;
        
        if (speed <=60) {
            result = 0;
        } else if (speed >=61 && speed <=80) {
            result = 1;
        } else {
            result = 2;
        }
        
        return result;
    }

	
	public static void main(String[] args) {
		System.out.println(caughtSpeeding(60, false));
		System.out.println(caughtSpeeding(65, false));
		System.out.println(caughtSpeeding(65, true));
	}

}
