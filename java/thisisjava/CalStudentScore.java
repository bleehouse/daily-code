import java.util.Scanner;

public class CalStudentScore {

	public static void main(String[] args) {
		boolean run = true;
		int studentNum = 0;
		int[] scores = null;
		Scanner scanner = new Scanner(System.in);
		
		while(run) {
			System.out.println("------------------------------------------------------------------");
			System.out.println("1. 학생수 | 2. 점수입력 | 3. 점수리스트 | 4. 분석 | 5. 종료");
			System.out.println("------------------------------------------------------------------");
			System.out.println("선택 > \r\n");
		
			int selectNo = scanner.nextInt();
			
			if (selectNo == 1) {System.out.println("학생수>\r\n");
				studentNum = scanner.nextInt();
				System.out.println("학생수 : " + String.valueOf(studentNum));
				scores = new int[studentNum];
			} else if (selectNo == 2) {

				for (int i = 0; i < scores.length; i++) {
					System.out.println("scores[" + String.valueOf(i) + "]\r\n");
					scores[i] = scanner.nextInt();
				}
				
				System.out.println("점수 입력 완료");
			} else if (selectNo == 3) {

				System.out.println(scores.length);
				for (int i = 0; i < scores.length; i++) {
					System.out.println("scores[" + String.valueOf(i) + "]" + String.valueOf(scores[i]));
				}
				
				System.out.println("점수리스트 출력완료");
			} else if (selectNo == 4) {
				
				int max = 0;
				int total = 0;
				int avg = 0;
				for (int i = 0; i < scores.length; i++) {
					if (max < scores[i]) {
						max = scores[i];
						total = total + scores[i];
					} 
				}
				avg = total / scores.length;
				
				System.out.println("최고점수 : " + max);
				System.out.println("평균 : " + avg);				
				
			} else if (selectNo == 5) {
				run = false;
				System.out.println("종료합니다.");
			}
		}
		scanner.close();
	}
}
