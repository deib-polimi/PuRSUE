package se.cth.pursue;

import java.io.BufferedWriter;
import java.io.FileWriter;

import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import org.antlr.v4.runtime.misc.Interval;

import static org.antlr.v4.runtime.CharStreams.fromFileName;
public class Main {
    public static void main(String[] args) throws Exception {
    	System.out.println("Parser UPPAAL to PYTHON started");
        CharStream in = fromFileName("./UPPAAL_plan.txt");
        
        int siz = in.size();
        int i = 0;
        boolean flag = true;
        String check = "";
        String checked = "";
        while ( i < siz && flag  ){
            Interval intervallo = new Interval(i, i+2);
           // System.out.println(intervallo);
            check = in.getText(intervallo);
           // System.out.println(check);
            if (check.equals(":\n\n")){
                Interval intervallo2 = new Interval(i+3, siz);
                checked = in.getText(intervallo2);
                flag = false;
                System.out.println("the total plan file is composed of "+siz+" characters, we remove the first "+(i+2) );
            }
            else{

                i++;
            }
        }
        CharStream cleansedIn = CharStreams.fromString(checked);


        


        UP2COLexer lexer = new UP2COLexer(cleansedIn);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        UP2COParser parser = new UP2COParser(tokens);
        
        parser.setBuildParseTree(false);

     	Controller controller = parser.controller().contr;

     	String output = controller.toString();

   		//System.out.println(stampare);
   		BufferedWriter writer = new BufferedWriter(new FileWriter("output_files/runtime_controller.py"));
		writer.write(output);

		writer.close();
        System.out.println("Parser UPPAAL to PYTHON finished");
    }
}