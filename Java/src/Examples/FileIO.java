			
package Examples;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class FileIO {

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		
		String message;
		
		BufferedWriter write = null;
		
		try {
			write = new BufferedWriter( new FileWriter("output.txt"));
			
			do {
				System.out.print("Enter in your message: ");
				message = scan.nextLine();
				write.write(message);
				System.out.println("Wrote: " + message + " to the file");
				write.write('\n');
			} while(!message.equals(""));
			
			write.close();
			System.out.println("Thank you for using ACM Writer");
		} catch (IOException e) {
			//The file could not be created
			e.printStackTrace();
		}

		scan.close();
		
	}

}