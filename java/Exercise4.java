import java.io.File;

public class Exercise4 {

	public static void main(String[] args) {
		File my_file_dir = new File("C:\\OneDriveTemp\\S-1-5-21-224592221-637395062-3764314592-1001\\new.bmp");
		if (my_file_dir.canWrite()) {
			System.out.println(my_file_dir.getAbsolutePath() + " can write.\n");
		} else {
			System.out.println(my_file_dir.getAbsolutePath() + " cannot write.\n");
		}
		if (my_file_dir.canRead()) {
			System.out.println(my_file_dir.getAbsolutePath() + " can read.\n");
		} else {
			System.out.println(my_file_dir.getAbsolutePath() + " cannot read.\n");
		}
	}

}
