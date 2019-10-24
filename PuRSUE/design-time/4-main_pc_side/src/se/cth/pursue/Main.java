package se.cth.pursue;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.lang.ProcessBuilder;
//import javax.annotation.Resource;
import java.util.Map.Entry;
import java.util.concurrent.TimeUnit;

import org.apache.http.client.ClientProtocolException;

import se.gu.MissionSender;

import org.apache.commons.io.FileUtils;

public class Main {

	public static void main(String[] args) throws ClientProtocolException, IOException, InterruptedException {
		System.out.println("This method performs the complete parsing from DSL to python controller, provided that the folder structure, file names and .jar files provided are conform to what's specified in readme.txt");

		


		
		String s = new String();
		// FIRST prcoess
		System.out.println("///////running first parser and UPPAAL//////");

		Runtime runt =  Runtime.getRuntime();


		ProcessBuilder p0 = new ProcessBuilder("java", "-jar", "DSL2UP.jar");
		p0.redirectErrorStream(true);
		Process processo0 = p0.start();

		BufferedReader stdInput0 = new BufferedReader(new InputStreamReader(processo0.getInputStream()));
		while ((s = stdInput0.readLine()) != null) {
			System.out.println(s);
		}


		processo0.waitFor();
		System.out.println("///////it finished////////");


		//second process
		System.out.println("///////running UP2CO///////");
		ProcessBuilder p1 = new ProcessBuilder("java", "-jar", "UP2CO.jar");
		p1.redirectErrorStream(true);
		Process processo1 = p1.start();

		BufferedReader stdInput1 = new BufferedReader(new InputStreamReader(processo1.getInputStream()));
		while ((s = stdInput1.readLine()) != null) {
			System.out.println(s);
		}


		processo1.waitFor();
		System.out.println("///////it finished////////");

		//third process
		System.out.println("///////running UP2OB///////");
		ProcessBuilder p2 = new ProcessBuilder("java", "-jar", "UP2OB.jar");
		p2.redirectErrorStream(true);
		Process processo2 = p2.start();
		BufferedReader stdInput2 = new BufferedReader(new InputStreamReader(processo2.getInputStream()));
		while ((s = stdInput2.readLine()) != null) {
			System.out.println(s);
		}


		processo2.waitFor();
		System.out.println("///////it finished///////");

		File controller = new File("./output_files/runtime_controller.py"); 
  		
  		File observer = new File ("./output_files/runtime_observer.py");

  		String controller_as_string = FileUtils.readFileToString(controller);
  		String observer_as_string = FileUtils.readFileToString(observer);
  		

		MissionSender sender = new MissionSender();


		String indirizzo = "192.168.1.140";
		String porta = "13000";

		sender.send(controller_as_string, indirizzo, porta);
		sender.send(observer_as_string, indirizzo, porta);

		System.out.println("finito!");
		
	
	}
}

