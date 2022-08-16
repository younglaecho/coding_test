import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class baek1064 {
	public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        
        String[] line = br.readLine().split(" "); // 첫 번째 라인을 받고 공백을 기준으로 나누기

        double x0 = (double) Integer.parseInt(line[0]);
        double y0 = (double) Integer.parseInt(line[1]);
        double x1 = (double) Integer.parseInt(line[2]);
        double y1 = (double) Integer.parseInt(line[3]);
        double x2 = (double) Integer.parseInt(line[4]);
        double y2 = (double) Integer.parseInt(line[5]);

        if (y0==y1 && y1==y2 && y2==y0) {
            System.out.println("-1.0");
        } else {
            double a = (x0-x1)/(y0-y1);
            double b = (x1-x2)/(y1-y2);
            double c = (x2-x0)/(y2-y0);
            if (a==b && b==c && c==a) {
                System.out.println("-1.0");
            }
            else {
                ArrayList<Double> lengths = new ArrayList<>();

                lengths.add(Math.sqrt(Math.pow((x0-x1), 2)+Math.pow((y0-y1), 2)));
                lengths.add(Math.sqrt(Math.pow((x1-x2), 2)+Math.pow((y1-y2), 2)));
                lengths.add(Math.sqrt(Math.pow((x2-x0), 2)+Math.pow((y2-y0), 2)));
    
                ArrayList<Double> result = new ArrayList<>();
    
                for (int i = 0; i < lengths.size(); i++) {
                    double total = 0;
                    for (int j = 0; j < lengths.size(); j++) {
                        if (i!=j) {
                            total += lengths.get(j);
                        }
                    }
                    result.add(total * 2);
                }
                double Max = Collections.max(result);
                double Min = Collections.min(result);
                System.out.println(Max-Min);
            }
            
        }

    }    
}
