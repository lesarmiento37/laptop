echo "
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0kxdoooooodxkOKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkol::;;,,,,,,;;;::cldxOKNWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWNOo:;,,;;,,,,,,,,,,,,,,,,,,;cox0XWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWKd:;;;;,;;;;;;;;;;;;;;;;;;;;;,,,;coOXWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMW0o;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::;;;cd0NMMMMMMMMMMMMMM
MMMMMMMMMMMWNWMMMMMMMMMWXx:;;;;;;;;;;;;;;;;;;;;;;;:ldxkO0KKK0Okxdk0NWMMMMMMMMMMM
MMMMMMMMMMNOd0MMMMMMMMMWXx:;;;;;;;;;;;;;;;;;;;;cokKXWWWWWWWMMMMMWNXXNWMMMMMMMMMM
MMMMMMMMWKd;:0MMMMMMMMMMNOc;;;;;;;;;;;;;;;;;:lkKNNKOxdooodxOXWMMMMMMMMMMMMMMMMMM
MMMMMMMNkc;';OWMMMMMMMMMWXx:;;;;;;;;;;;;;;;:xXN0xo:;;;;;;;;;cdKWMMMMMMMMMMMMMMMM
MMMMMWXd:;,''dNMMMMMMMMMMWXkc;;;;;;;;;;;;;;;ldo:;;;;;;;;;;;;;;cxXMMMMMMMMMMMMMMM
MMMMWKo;;;,'.:0MMMMMMMMMMMMWKd:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:dXMMMMMMMMNNWMMM
MMMW0l;;;;,'''lXMMMMMMMMMMMMWN0d:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:xNMMMMMMMXOKMMM
MMWKl;;;;;,''',oXMMMMMMMMMMMMMMN0o:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;lKMMMMMMMXddXMM
MMXo;;;;;;;,''',lKWMMMMMMMMMMMMMWN0o:;;;;;;;;;;;;;;;;;;;;;;;;;;;;lKMMMMMMMKo:xNM
MNx:;;;;;;;,'''',cOWMMMMMMMMMMMMMMWNOo:;;;;;;;;;;;;;;;;;;;;;;;;;;dNMMMMMMWOc;cOW
W0c;;;;;;;;;,,,,,,:xXWMMMMMMMMMMMMMMWXOo::;;;;;;;;;;;;;;;;;;;;;;oKWMMMMMWKo;;;dX
Nd;;;;;;;;;;,,,,,,,;lONMMMMMMMMMMMMMMMWXKkl;;;;;;;;;;;;;;;;;;;:dXWMMMMMW0l;,;;cO
0l;;;;;;;;;;;,,,,,,,,;o0WMMMMMMMMMMMMMMMMWKd:;;;;;;;;;;;;;;;:o0NMMMMMWXxc;;;;;;x
k:;;;;;;;;;;;;;,,,,,,,,:d0NMMMMMMMMMMMMMMMWNkc;;;;;;;;;;;:lx0NMMMMMN0xc;;;;;,,;o
x:;;;;;;;;;;;;;;;,,,,,,,,:d0WMMMMMMMMMMMMMMMNOl;;;;;;cldk0NWMMMMMWKxc;;;;;;;,,,l
x;;;;;;;;;;;;;;;;;;,,,,,,,;:dKWMMMMMMMMMMMMMMNkc;;;;;d0KKXNWMMMMMWWX0ko:;;;;;,,l
x:;;;;;;;;;;;;;;;;;;;;;;,;;;;ckXWMMMMMMMMMMMMWXx:,;;;:cccclox0NMMMMMMWNKxc;;;,,l
O:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oKWMMMMMMMMMMMMW0l;,;;;;;;;;;;:oONMMMMMMMW0o;;,,o
Kl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;l0WMMMMMMMMMMMWXd;;;;;;;;;;;;;;:dXWMMMMMMWKo;,;k
Nx;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMMMMMMMMWXx:;;;;;;;;;;;;;;;oXMMMMMMMWOc,cK
W0l;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;cOWMMMMMMMMMMWXd;;;;;;;;;;;;;;;;:xNMMMMMMWKl;xW
MNk:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:OWMMMMMMMMMMW0l;,;;;;;;;;;;;;;;;c0WMMMMMWKllKM
MMXd;;;;;;;;;;;;;;;;;;;;;;;;;;;;;lKMMMMMMMMMMWXx:,;;;;;;;;;;;;;;;;;xNMMMMMW0dOWM
MMMKo;;;;;;;;;;;;;;;;;;;;;;;;;;;:kNMMMMMMMMMWNkc,;;;;;;;;;;;;;;;;;;xNMMMMMWO0WMM
MMMWKo;;;;;;;;;;;;;;;;;;;;;;;;;:xNMMMMMMMMMWXkc;,;;;;;;;;;;;;;;;;;:xNMMMMMNXWMMM
MMMMWKo;;;;;;;;;;;;;;;;;;;;;;;lkNMMMMMMMMMWKd:,,;;;;;;;;;;;;;;;;;;c0WMMMMWWWMMMM
MMMMMWXd:;;;;;;;;;;;;;;;;;;:lkXWMMMMMMMWNXkc;,,,;,;;;;;;;;;;;;;;;:kNMMMMMMMMMMMM
MMMMMMMNOl;;;;;;;;;;;;;:cok0NWMMMMMMWNKxoc;,,,,;,,;;;;;;;;;;;;;;:xXMMMMMMMMMMMMM
MMMMMMMMWXOxxdooooddxkOKNWMMMMMMMWN0xl:,,,,,,,,,;;;;;;;;;;;;;;;ckNMMMMMMMMMMMMMM
MMMMMMMMMMMMMWWWWWWWWMMMMMMWWXKOxoc;,,,,,,,,,,,,;;;;;;;;;;;;;:dKWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWX000OOOkxxdlc:;,'',,,,,,,,,,,;;;;;;;;;;;;;;:oONMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWXOoc;,,''''''',,,,,,,,,;;;;;;;;;;;;;;;;;;cd0NMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWXOxoc;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;cdOXWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWNX0kdlc:;;;;;;;;;;;;;;;;;;:cldk0XWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWNKOxdlc:;;;;;;;;:cloxOKNWWMMMMMMMMMMMMMMMMMMMMMMMMMMM
"
sleep 2;

rm /home/dionis/1*

nmap 192.168.19.60 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n19' ssh admin@192.168.19.60 'system health print file=192.168.19.60;tool fetch address=10.255.0.70 src-path=192.168.19.60.txt user=dionis mode=ftp password=dionis dst-path="192.168.19.60.txt" upload=yes'
	else
	   touch /home/dionis/192.168.19.60.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.19.60.txt
	fi

nmap 192.168.19.52 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n19' ssh admin@192.168.19.52 'system health print file=192.168.19.52;tool fetch address=10.255.0.70 src-path=192.168.19.52.txt user=dionis mode=ftp password=dionis dst-path="192.168.19.52.txt" upload=yes'
	else
	   touch /home/dionis/192.168.19.52.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.19.52.txt
	fi

nmap 192.168.19.163 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n19' ssh admin@192.168.19.163 'system health print file=192.168.19.163;tool fetch address=10.255.0.70 src-path=192.168.19.163.txt user=dionis mode=ftp password=dionis dst-path="192.168.19.163.txt" upload=yes'
	else
	   touch /home/dionis/192.168.19.163.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.19.163.txt
	fi

nmap 192.168.19.65 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n19' ssh admin@192.168.19.65 'system health print file=192.168.19.65;tool fetch address=10.255.0.70 src-path=192.168.19.65.txt user=dionis mode=ftp password=dionis dst-path="192.168.19.65.txt" upload=yes'
	else
	   touch /home/dionis/192.168.19.65.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.19.65.txt
	fi

nmap 192.168.19.181 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n19' ssh admin@192.168.19.181 'system health print file=192.168.19.181;tool fetch address=10.255.0.70 src-path=192.168.19.181.txt user=dionis mode=ftp password=dionis dst-path="192.168.19.181.txt" upload=yes'
	else
	   touch /home/dionis/192.168.19.181.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.19.181.txt
	fi

nmap 192.168.19.93 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n19' ssh admin@192.168.19.93 'system health print file=192.168.19.93;tool fetch address=10.255.0.70 src-path=192.168.19.93.txt user=dionis mode=ftp password=dionis dst-path="192.168.19.93.txt" upload=yes'
	else
	   touch /home/dionis/192.168.19.93.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.19.93.txt
	fi

nmap 192.168.19.87 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n19' ssh admin@192.168.19.87 'system health print file=192.168.19.87;tool fetch address=10.255.0.70 src-path=192.168.19.87.txt user=dionis mode=ftp password=dionis dst-path="192.168.19.87.txt" upload=yes' 
	else
	   touch /home/dionis/192.168.19.87.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.19.87.txt
	fi

nmap 192.168.19.153 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n19' ssh admin@192.168.19.153 'system health print file=192.168.19.153;tool fetch address=10.255.0.70 src-path=192.168.19.153.txt user=dionis mode=ftp password=dionis dst-path="192.168.19.153.txt" upload=yes' 
	else
	   touch /home/dionis/192.168.19.153.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.19.153.txt
	fi

nmap 192.168.21.103 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n21' ssh admin@192.168.21.103 'system health print file=192.168.21.103;tool fetch address=10.255.0.70 src-path=192.168.21.103.txt user=dionis mode=ftp password=dionis dst-path="192.168.21.103.txt" upload=yes' 
	else
	   touch /home/dionis/192.168.21.103.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.21.103.txt
	fi

nmap 192.168.35.212 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
            sshpass -p 'N3tG3st10n35' ssh admin@192.168.35.212 'system health print file=192.168.35.212;tool fetch address=10.255.0.70 src-path=192.168.35.212.txt user=dionis mode=ftp password=dionis dst-path="192.168.35.212.txt" upload=yes'
	else
	   touch /home/dionis/192.168.35.212.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.35.212.txt
	fi

nmap 192.168.4.30 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
           sshpass -p 'N3tG3st10n04' ssh admin@192.168.4.30 'system health print file=192.168.4.30;tool fetch address=10.255.0.70 src-path=192.168.4.30.txt user=dionis mode=ftp password=dionis dst-path="192.168.4.30.txt" upload=yes'
	else
	   touch /home/dionis/192.168.4.30.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.4.30.txt
	fi

nmap 192.168.4.130 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n04' ssh admin@192.168.4.130 'system health print file=192.168.4.130;tool fetch address=10.255.0.70 src-path=192.168.4.130.txt user=dionis mode=ftp password=dionis dst-path="192.168.4.130.txt" upload=yes'
	else
	   touch /home/dionis/192.168.4.130.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.4.130.txt
	fi

nmap 192.168.4.163 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n04' ssh admin@192.168.4.163 'system health print file=192.168.4.163;tool fetch address=10.255.0.70 src-path=192.168.4.163.txt user=dionis mode=ftp password=dionis dst-path="192.168.4.163.txt" upload=yes' 
	else
	   touch /home/dionis/192.168.4.163.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.4.163.txt
	fi

nmap 192.168.4.26 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
           sshpass -p 'N3tG3st10n04' ssh admin@192.168.4.26 'system health print file=192.168.4.26;tool fetch address=10.255.0.70 src-path=192.168.4.26.txt user=dionis mode=ftp password=dionis dst-path="192.168.4.26.txt" upload=yes'
	else
	   touch /home/dionis/192.168.4.26.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.4.26.txt
	fi

nmap 192.168.4.100 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n04' ssh admin@192.168.4.100 'system health print file=192.168.4.100;tool fetch address=10.255.0.70 src-path=192.168.4.100.txt user=dionis mode=ftp password=dionis dst-path="192.168.4.100.txt" upload=yes'
	else
	   touch /home/dionis/192.168.4.100.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.4.100.txt
	fi

nmap 192.168.9.81 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n09' ssh admin@192.168.9.81 'system health print file=192.168.9.81;tool fetch address=10.255.0.70 src-path=192.168.9.81.txt user=dionis mode=ftp password=dionis dst-path="192.168.9.81.txt" upload=yes'
	else
	   touch /home/dionis/192.168.9.81.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.9.81.txt
	fi

nmap 192.168.9.199 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n09' ssh admin@192.168.9.199 'system health print file=192.168.9.199;tool fetch address=10.255.0.70 src-path=192.168.9.199.txt user=dionis mode=ftp password=dionis dst-path="192.168.9.199.txt" upload=yes'
	else
	   touch /home/dionis/192.168.9.199.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.9.199.txt
	fi

nmap 192.168.9.140 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n09' ssh admin@192.168.9.140 'system health print file=192.168.9.140;tool fetch address=10.255.0.70 src-path=192.168.9.140.txt user=dionis mode=ftp password=dionis dst-path="192.168.9.140.txt" upload=yes'
	else
	   touch /home/dionis/192.168.9.140.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.9.140.txt
	fi

nmap 192.168.16.170 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n16' ssh admin@192.168.16.170 'system health print file=192.168.16.170;tool fetch address=10.255.0.70 src-path=192.168.16.170.txt user=dionis mode=ftp password=dionis dst-path="192.168.16.170.txt" upload=yes'
	else
	   touch /home/dionis/192.168.16.170.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.16.170.txt
	fi

nmap 192.168.16.117 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n16' ssh admin@192.168.16.117 'system health print file=192.168.16.117;tool fetch address=10.255.0.70 src-path=192.168.16.117.txt user=dionis mode=ftp password=dionis dst-path="192.168.16.117.txt" upload=yes'
	else
	   touch /home/dionis/192.168.16.117.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.16.117.txt
	fi

nmap 192.168.1.54 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n01' ssh admin@192.168.1.54 'system health print file=192.168.1.54;tool fetch address=10.255.0.70 src-path=192.168.1.54.txt user=dionis mode=ftp password=dionis dst-path="192.168.1.54.txt" upload=yes' 
	else
	   touch /home/dionis/192.168.1.54.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.1.54.txt
	fi

nmap 192.168.1.43 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n01' ssh admin@192.168.1.43 'system health print file=192.168.1.43;tool fetch address=10.255.0.70 src-path=192.168.1.43.txt user=dionis mode=ftp password=dionis dst-path="192.168.1.43.txt" upload=yes'  
	else
	   touch /home/dionis/192.168.1.43.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.1.43.txt
	fi

nmap 192.168.1.32 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
            sshpass -p 'N3tG3st10n01' ssh admin@192.168.1.32 'system health print file=192.168.1.32;tool fetch address=10.255.0.70 src-path=192.168.1.32.txt user=dionis mode=ftp password=dionis dst-path="192.168.1.32.txt" upload=yes'
	else
	   touch /home/dionis/192.168.1.32.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.1.32.txt
	fi

nmap 192.168.1.78 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
            sshpass -p 'N3tG3st10n01' ssh admin@192.168.1.78 'system health print file=192.168.1.78;tool fetch address=10.255.0.70 src-path=192.168.1.78.txt user=dionis mode=ftp password=dionis dst-path="192.168.1.78.txt" upload=yes'
	else
	   touch /home/dionis/192.168.1.78.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.1.78.txt
	fi

nmap 192.168.1.54 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
           sshpass -p 'N3tG3st10n01' ssh admin@192.168.1.54 'system health print file=192.168.1.54;tool fetch address=10.255.0.70 src-path=192.168.1.54.txt user=dionis mode=ftp password=dionis dst-path="192.168.1.54.txt" upload=yes'
	else
	   touch /home/dionis/192.168.1.54.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.1.54.txt
	fi

nmap 192.168.5.193 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
           sshpass -p 'N3tG3st10n05' ssh admin@192.168.5.193 'system health print file=192.168.5.193;tool fetch address=10.255.0.70 src-path=192.168.5.193.txt user=dionis mode=ftp password=dionis dst-path="192.168.5.193.txt" upload=yes' 
	else
	   touch /home/dionis/192.168.5.193.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.5.193.txt
	fi

nmap 192.168.5.140 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
           sshpass -p 'N3tG3st10n05' ssh admin@192.168.5.140 'system health print file=192.168.5.140;tool fetch address=10.255.0.70 src-path=192.168.5.140.txt user=dionis mode=ftp password=dionis dst-path="192.168.5.140.txt" upload=yes'
	else
	   touch /home/dionis/192.168.5.140.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.5.140.txt
	fi

nmap 192.168.30.33 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
           sshpass -p 'N3tG3st10n30' ssh admin@192.168.30.33 'system health print file=192.168.30.33;tool fetch address=10.255.0.70 src-path=192.168.30.33.txt user=dionis mode=ftp password=dionis dst-path="192.168.30.33.txt" upload=yes'
	else
	   touch /home/dionis/192.168.30.33.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.30.33.txt
	fi

nmap 192.168.5.89 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
           sshpass -p 'N3tG3st10n05' ssh admin@192.168.5.89 'system health print file=192.168.5.89;tool fetch address=10.255.0.70 src-path=192.168.5.89.txt user=dionis mode=ftp password=dionis dst-path="192.168.5.89.txt" upload=yes'
	else
	   touch /home/dionis/192.168.5.89.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.5.89.txt
	fi

nmap 192.168.19.177 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
           sshpass -p 'N3tG3st10n19' ssh admin@192.168.19.177 'system health print file=192.168.19.177;tool fetch address=10.255.0.70 src-path=192.168.19.177.txt user=dionis mode=ftp password=dionis dst-path="192.168.19.177.txt" upload=yes'
	else
	   touch /home/dionis/192.168.19.177.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.19.177.txt
	fi

nmap 192.168.9.79 -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
         sshpass -p 'N3tG3st10n09' ssh admin@192.168.9.79 'system health print file=192.168.9.79;tool fetch address=10.255.0.70 src-path=192.168.9.79.txt user=dionis mode=ftp password=dionis dst-path="192.168.9.79.txt" upload=yes'
	else
	   touch /home/dionis/192.168.9.79.txt 	
	   echo "   voltage: 0V " >> /home/dionis/192.168.9.79.txt
	fi

nmap 192.168.35.63 -PN -p ssh | egrep 'open'
        if [ $? -eq 0 ]
        then
         sshpass -p 'N3tG3st10n35' ssh admin@192.168.35.63 'system health print file=192.168.35.63;tool fetch address=10.255.0.70 src-path=192.168.35.63.txt user=dionis mode=ftp password=dionis dst-path="192.168.35.63.txt" upload=yes'
        else
           touch /home/dionis/192.168.35.63.txt
           echo "   voltage: 0V " >> /home/dionis/192.168.35.63.txt
        fi

javac testvol/testvol.java
java testvol.testvol

javac testvol/testvol2.java
java  testvol.testvol2

javac testvol/testvol3.java
java  testvol.testvol3

python testigosp.py
#expect ftp.sh
