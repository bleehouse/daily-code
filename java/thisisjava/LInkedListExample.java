// ArrayList와 LinkedList의 실행 성능 비교
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class LInkedListExample {

	public static void main(String[] args) {
		List<String> list1 = new ArrayList<String>();
		List<String> list2 = new LinkedList<String>();
		
		long startTime;
		long endTime;
		
		startTime = System.nanoTime();
		
		for(int i=0; i<1000; i++){
			list1.add(String.valueOf(i));
		}
		
		endTime = System.nanoTime();
		
		System.out.println("ArrayList �ɸ��ð� : " + (endTime - startTime) + " ns");
		
		startTime = System.nanoTime();
		
		for(int i=0; i<1000; i++){
			list2.add(String.valueOf(i));
		}

		endTime = System.nanoTime();
		
		System.out.println("LinkedList �ɸ��ð� : " + (endTime - startTime) + " ns");		
	}

}
