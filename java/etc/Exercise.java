import java.io.File;

public class Exercise {

	public static void main(String[] args) {
		File file = new File("c:\\work");
		String[] filelist = file.list();
		
		for (String name:filelist) {
			System.out.println(name);
		}
	}
}
