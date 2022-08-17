import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;


public class baek1049 {
	public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] line = br.readLine().split(" "); // 첫 번째 라인을 받고 공백을 기준으로 나누기

        int cut = Integer.parseInt(line[0]);
        int brand = Integer.parseInt(line[1]);


        ArrayList<Integer> setList = new ArrayList<>();
        ArrayList<Integer> oneList = new ArrayList<>();

        for (int i = 0; i < brand ; i ++ ) {
            String[] a = br.readLine().split(" ");
            setList.add(Integer.parseInt(a[0]));
            oneList.add(Integer.parseInt(a[1]));
        }

        int setMin = Collections.min(setList);
        int oneMin = Collections.min(oneList);

        int result = 0;
        int mod = 0;
        if (setMin > oneMin * 6) {
            System.out.println(oneMin*cut);
        } else {
            result += (cut / 6);
            result = result*setMin;
            mod = cut % 6;
            if (mod*oneMin <= setMin) {
                result += mod*oneMin;
            } else {
                result += setMin;
            }
            System.out.println(result);
        }
    }    
}
