
package testvol;
import java.util.*;
import java.util.Scanner;  // Import the Scanner class
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.File;
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.util.concurrent.TimeUnit;

public class testvol {

	  public static void main(String[] args) {
		 String[] rutas = {"/home/dionis/192.168.19.60.txt","/home/dionis/192.168.19.52.txt","/home/dionis/192.168.19.244.txt","/home/dionis/192.168.19.197.txt","/home/dionis/192.168.19.181.txt","/home/dionis/sarzo.txt","/home/dionis/192.168.19.87.txt","/home/dionis/192.168.19.153.txt","/home/dionis/192.168.21.103.txt","/home/dionis/192.168.35.212.txt","/home/dionis/192.168.4.30.txt","/home/dionis/192.168.4.130.txt","/home/dionis/192.168.4.163.txt","/home/dionis/192.168.4.26.txt","/home/dionis/192.168.4.100.txt","/home/dionis/192.168.9.81.txt","/home/dionis/192.168.9.199.txt","/home/dionis/192.168.9.140.txt","/home/dionis/192.168.9.79.txt","/home/dionis/192.168.16.170.txt","/home/dionis/192.168.16.56.txt","/home/dionis/192.168.1.54.txt","/home/dionis/192.168.1.46.txt","/home/dionis/192.168.1.32.txt","/home/dionis/192.168.1.78.txt","/home/dionis/192.168.5.193.txt","/home/dionis/192.168.5.140.txt","/home/dionis/192.168.5.89.txt","/home/dionis/192.168.30.5.txt"};
	  String[] nombres = {"manjui","quinini","cerro negro","guaduas","flores","sarzo","granada","flandes","tierra morada","bethesda","guadalupe","santo domingo","alpes","boqueron","av 19","suba 2","tibitoc","horgano","junin","cazadores","margarita","picacho","soldapedro","petalos","tablazo","soda","suba1","cucunuba","tres cruces"};
 Double[] voltajes = new Double[rutas.length];
 String[] volstr = new String[rutas.length];

		 for(int n = 0;n<rutas.length;n++){
			     File fichero = new File(rutas[n]);
			         Scanner s = null;
				     String voltaje ="";
				                     
				     try {
					           s = new Scanner(fichero);

						        while (s.hasNextLine()) {
								     String linea = s.nextLine();
								          String linea2 = linea;                            
									       if(linea2.matches(".*voltage.*$")){
                                                voltaje = linea2.replace(" ", "");
                                                String volfin = voltaje.replace("voltage:", "");
                                                String volfin2 = volfin.replace("V","");
                                                String volfin3 = volfin2.replace(".",",");
                                                volstr[n] = volfin3;
                                                double vold = Double.parseDouble(volfin2);
                                                voltajes[n] = vold;
                                                       if(vold < 1)
                                                       {
                                                        System.out.println(/*nombres[n]+"|          "+*/volstr[n]+";"+"Alarmado");
                                                       }
                                                       else if((vold>22)&&(vold<23.9))
                                                       {
                                                        System.out.println(/*nombres[n]+"|          "+*/volstr[n]+";"+"Amarillo");
                                                       }
                                                       else if ((vold>1)&&(vold<22))
                                                       {
                                                        System.out.println(/*nombres[n]+"|          "+*/volstr[n]+";"+"Naranja");
                                                       }
                                                       else
                                                       {
                                                        System.out.println(/*nombres[n]+      |           "*/volstr[n]+";"+"OK");
                                                       }
												
												//System.out.println(n+"    "+"|"+nombres[n]+"|"+"  "+" "+"|"+voltajes[n]+"|");
														                                       
														                 }	
							}

				     } catch (Exception ex) {
				    ///System.out.println("Mensaje: " + ex.getMessage());
				     } finally {
				     			
				     			try {
				     			     if (s != null)
				     			          s.close();
				     			          } catch (Exception ex2) {
				     			              System.out.println("Mensaje 2: " + ex2.getMessage());
				     			              			}
				    			              					}
				    			              		        }      
				     			           	  }
				     			  }
				     
