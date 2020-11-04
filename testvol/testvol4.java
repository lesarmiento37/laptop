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
public class testvol4 {

    public static void main(String[] args) {
       String[] rutas = {"/home/dionis/192.168.19.60.txt","/home/dionis/192.168.19.52.txt","/home/dionis/192.168.19.163.txt","/home/dionis/192.168.19.65.txt","/home/dionis/192.168.19.181.txt","/home/dionis/192.168.19.152.txt","/home/dionis/192.168.19.87.txt","/home/dionis/192.168.19.153.txt","/home/dionis/192.168.21.103.txt","/home/dionis/192.168.35.212.txt","/home/dionis/192.168.4.30.txt","/home/dionis/192.168.4.130.txt","/home/dionis/192.168.4.163.txt","/home/dionis/192.168.4.26.txt","/home/dionis/192.168.4.100.txt","/home/dionis/192.168.9.81.txt","/home/dionis/192.168.9.199.txt","/home/dionis/192.168.9.140.txt","/home/dionis/192.168.9.79.txt","/home/dionis/192.168.16.170.txt","/home/dionis/192.168.16.117.txt","/home/dionis/192.168.1.54.txt","/home/dionis/192.168.1.43.txt","/home/dionis/192.168.1.32.txt","/home/dionis/192.168.1.78.txt","/home/dionis/192.168.5.193.txt","/home/dionis/192.168.5.140.txt","/home/dionis/192.168.5.89.txt","/home/dionis/192.168.30.33.txt","/home/dionis/192.168.35.63.txt"};
       String[] nombres = {"Manjui","Quinini","Cerro Negro","Guaduas","Flores","Sarzo","Granada","Flandes","Tierra Morada","Bethesda","Guadalupe","Santo domingo","Alpes","Boqueron","Av 19","Suba 2","Tibitoc","Horgano","Junin","Cazadores","Margarita","Picacho","Soldapedro","Petalos","Tablazo","Soda","Suba1","Cucunuba","Tres Cruces","Eduardo Porras"};
       
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
                                                        System.out.println(nombres[n]+";"+ volstr[n]+";"+"Alarmado");
                                                       }
                                                       else if((vold>22)&&(vold<23.9))
                                                       {
                                                        System.out.println(nombres[n]+";"+ volstr[n]+";"+"Amarillo");
                                                       }
                                                       else if ((vold>1)&&(vold<22))
                                                       {
                                                        System.out.println(nombres[n]+";"+ volstr[n]+";"+"Naranja");
                                                       }
                                                       else
                                                       {
                                                        System.out.println(nombres[n]+      ";"    + volstr[n]+";"+"OK");
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
