import java.util.HashMap;

public class MaxSpanExample {

	public static void main(String[] args) {

		System.out.println(maxSpan(new int[] {1, 2, 1, 1, 3}));
		System.out.println(maxSpan(new int[] {1, 4, 2, 1, 4, 1, 4}));
		System.out.println(maxSpan(new int[] {1, 4, 2, 1, 4, 4, 4}));
		System.out.println(maxSpan(new int[] {3, 3, 3}));
		System.out.println(maxSpan(new int[] {3, 9, 3}));
		System.out.println(maxSpan(new int[] {3, 9, 9}));
		System.out.println(maxSpan(new int[] {3, 9}));
		System.out.println(maxSpan(new int[] {3, 3}));
		System.out.println(maxSpan(new int[] {}));
		System.out.println(maxSpan(new int[] {1}));
		
	}

	public static int maxSpan(int[] nums) {
		  
		  HashMap<String, String> map = new HashMap<String, String>();
		  
		  int maxspan = 1;
		  
		  if (nums.length == 0 ){
		    maxspan = 0;
		  } else {
		      for (int i=0; i < nums.length; i++) {

		      if (!map.containsKey(String.valueOf(nums[i]))) {
		        map.put(String.valueOf(nums[i]), String.valueOf(i) + "_" + String.valueOf(i));
		      } else {
		     
		        String value = map.get(String.valueOf(nums[i])).substring(0, 1);
		     
		        map.put(
		          String.valueOf(nums[i]), 
		          value + "_" + String.valueOf(i)
		        );
		       maxspan = (i + 1) - Integer.parseInt(value);
		      }
		    }
		  }
		  
		  return maxspan;
		}	
	
}
