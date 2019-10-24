package se.cth.pursue;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.Map.Entry;
import java.util.MissingResourceException;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.xtext.generator.GeneratorDelegate;
import org.eclipse.xtext.generator.InMemoryFileSystemAccess;
import org.eclipse.xtext.resource.XtextResource;
import org.eclipse.xtext.resource.XtextResourceSet;
import org.eclipse.xtext.validation.*;
import se.cth.PursueStandaloneSetup;

import com.google.inject.Injector;

import java.util.concurrent.TimeUnit;


public class Main {

	public static void main(String[] args) throws  IOException, MissingResourceException {
		System.out.println("This method takes as input a .pur file specifying the system and outputs a controller guaranteeing to always satisify the goal");
		//

		//define timer variables
		long startTime = 0;
		long endTime =0;
		long elapsedTime = 0;


		//massi inizio timer qui

		startTime = System.currentTimeMillis();
		// inizializzo parser
		Injector iniettore = new PursueStandaloneSetup().createInjectorAndDoEMFRegistration();

		// if file was specified use that one, otherwise use standard one
	String file_location;
		//if (args.length==0)
			file_location = "./input_language/default_input.pur";
		//else
		//	file_location = "./input_language/" + args[0];		

		// check che funga, va la
		System.out.println("considering source file:" + file_location);

		// tirar fuori la risosorsa
		// esco il resource set
		XtextResourceSet risorsaSet = iniettore.getInstance(XtextResourceSet.class);
		// nel file d'esempio qeuesto c'era, togliendolo funge comunque... lo ascio che
		// si sa mai
		risorsaSet.addLoadOption(XtextResource.OPTION_RESOLVE_ALL, Boolean.TRUE);

		// esco l'URI
		URI resource_URI =  URI.createFileURI(file_location);
		// creo risorsa
		Resource resource = risorsaSet.getResource(resource_URI, true);

		// validation
		
		 IResourceValidator validatore = iniettore.getInstance(IResourceValidator.class); 
		 List<Issue> report =validatore.validate(resource, CheckMode.ALL, null );		 
		 
		if (report.isEmpty()) {
			System.out.println("validation succeded");

		// creo generatore(usando il Delegate che mi facilita la vita)
		GeneratorDelegate delegato = iniettore.getInstance(GeneratorDelegate.class);

		// creo FSA
		InMemoryFileSystemAccess fsa = new InMemoryFileSystemAccess();
		// generazione
		delegato.doGenerate(resource, fsa);

		/// manca la creazione vera del file xD
		String[] nomi = new String[2];
		nomi[0] = "UPPAAL_model.q";
		nomi[1] = "UPPAAL_model.xml";
		int i =0;
		if (args.length != 0 && args[0].equals("custom_property")){
			System.out.println("using custom property already positioned by user in folder");
			nomi[0] ="system_generated_property.q";
		}
		for (Entry<String, CharSequence> file : fsa.getTextFiles().entrySet()) {

			BufferedWriter writer = new BufferedWriter(new FileWriter("UPPAAL/"+nomi[i]));
			writer.write(file.getValue().toString());
			i++;
			writer.close();


		}
		endTime = System.currentTimeMillis();
		elapsedTime = endTime - startTime;
		System.out.println("UPPAAL model crated in "+elapsedTime+" milliseconds");

		// esecuzione di verifyTGA


		String s = null;
		String output = null;
		boolean flag = true;


		startTime = System.currentTimeMillis();
		Process p = Runtime.getRuntime().exec("./UPPAAL/verifytga -t0 UPPAAL/UPPAAL_model.xml");

		BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));


		while (flag && (s = stdInput.readLine()) != null) {
			System.out.println(s);
			output = output + s + "\n";
			if (s.equals("Strategy to win:") || s.equals("Strategy to avoid losing:")) {
				flag = false;	
				endTime = System.currentTimeMillis();
				elapsedTime = endTime - startTime;
				System.out.println( "plan created in " + elapsedTime +" milliseconds");
			}

		}
		startTime = System.currentTimeMillis();
		while ((s = stdInput.readLine())!= null) {
			output = output + s + "\n";
		}
		
		BufferedWriter writer = new BufferedWriter(new FileWriter("UPPAAL_plan.txt"));
		writer.write(output);

		writer.close();
		endTime = System.currentTimeMillis();
		elapsedTime = endTime - startTime;
		System.out.println( "plan printed to file in " + elapsedTime+" milliseconds");
		//sender.send(messaggio, indirizzo, porta);



		 }
		else {
			System.out.println("input file not conform to grammar rules. Issues detected:");
			for(Issue problema: report) {
					System.out.println(problema);
			}
		}
	}
}
