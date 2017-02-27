import java.io.File;
import java.io.FilenameFilter;

public class Exercise2 {

	public static void main(String[] args) {
		File file = new File("c:\\work");
		String[] list = file.list(new FilenameFilter() {
			@Override
			public boolean accept(File dir, String name) {
				if (name.toLowerCase().endsWith(".js")) {
					return true;
				} else {
					return false;
				}
			}
		});
        
		for (String f : list) {
			System.out.println(f);
		}
	}
}
