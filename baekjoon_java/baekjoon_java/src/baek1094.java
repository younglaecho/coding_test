import java.util.Scanner;

public class baek1094 {
	public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        
        String binary = Integer.toBinaryString(number);

        int answer = 0;

        for(int i = 0; i < binary.length(); i++) {
            answer += Integer.valueOf(Integer.parseInt(String.valueOf(binary.charAt(i))));
        }

        System.out.println(answer);
        sc.close();
    }
}