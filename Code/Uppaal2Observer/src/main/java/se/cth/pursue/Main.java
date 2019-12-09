package se.cth.pursue;

import java.io.BufferedWriter;
import java.io.FileWriter;

import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;


import static org.antlr.v4.runtime.CharStreams.fromFileName;
public class Main {
    public static void main(String[] args) throws Exception {
    	System.out.println("Parser UPPAAL to OBSERVER started");
        CharStream in = fromFileName("./UPPAAL/UPPAAL_model.xml");
        UP2OBLexer lexer = new UP2OBLexer(in);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        UP2OBParser parser = new UP2OBParser(tokens);
        
        parser.setBuildParseTree(true);

     	Model model = parser.model().mod;

     	String output = model.toString();

   		//System.out.println(stampare);
   		BufferedWriter writer = new BufferedWriter(new FileWriter("output_files/runtime_observer.py"));
		writer.write(output);

		writer.close();
        System.out.println("Parser UPPAAL to OBSERVER finished");
    }
}