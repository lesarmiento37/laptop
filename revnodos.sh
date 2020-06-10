#!/bin/bash

rm /home/dionis/mo*

for n in 111 93 183 77 113 12 145 30 124 151 53 98 160 45 14 188 38 39 17 176 216 23 160 74 195 27 240 218 57 116 233 22
do
nmap 192.168.16.$n  -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n16' ssh admin@192.168.16.$n "/interface wireless monitor numbers=0 file=m192.168.16.N;tool fetch address=10.255.0.70 src-path=m192.168.16.N.txt user=dionis mode=ftp password=dionis dst-path="mo192.168.16.$n.txt" upload=yes;quit"
	else
	   touch /home/dionis/mo192.168.16.$n.txt
	   echo "   voltage: 0V " >> /home/dionis/mo192.168.16.$n.txt
	fi
done

for n in 84 153 102 158 32 13 141 200 63 169 59 131 91 52 198 115 81 82
do
nmap 192.168.21.$n  -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n21' ssh admin@192.168.21.$n "/interface wireless monitor numbers=0 file=m192.168.21.N;tool fetch address=10.255.0.70 src-path=m192.168.21.N.txt user=dionis mode=ftp password=dionis dst-path="mo192.168.21.$n.txt" upload=yes;quit"
	else
	   touch /home/dionis/mo192.168.21.$n.txt
	   echo "   voltage: 0V " >> /home/dionis/mo192.168.21.$n.txt
	fi
done


for n in 141 85 131 124 118 11 92 83 200 183 200 183 23 135 111 227 151 179 10 120 46
do
nmap 192.168.19.$n  -PN -p ssh | egrep 'open'
	if [ $? -eq 0 ]
	then
          sshpass -p 'N3tG3st10n19' ssh admin@192.168.19.$n "/interface wireless monitor numbers=0 file=m192.168.19.N;tool fetch address=10.255.0.70 src-path=m192.168.19.N.txt user=dionis mode=ftp password=dionis dst-path="mo192.168.19.$n.txt" upload=yes;quit"
	else
	   touch /home/dionis/mo192.168.19.$n.txt
	   echo "   voltage: 0V " >> /home/dionis/mo192.168.19.$n.txt
	fi
done

for n in 183 190 41 75 35 135 83 129 18 232 84 180 248 50 152 223 117
do
nmap 192.168.4.$n  -PN -p ssh | egrep 'open'
        if [ $? -eq 0 ]
        then
          sshpass -p 'N3tG3st10n04' ssh admin@192.168.4.$n "/interface wireless monitor numbers=0 file=m192.168.4.N;tool fetch address=10.255.0.70 src-path=m192.168.4.N.txt user=dionis mode=ftp password=dionis dst-path="mo192.168.4.$n.txt" upload=yes;quit"
        else
           touch /home/dionis/mo192.168.4.$n.txt
           echo "   voltage: 0V " >> /home/dionis/mo192.168.4.$n.txt
        fi
done

for n in 176 170 65 71 127 16 133 69 34 9 213 135 20
do
nmap 192.168.35.$n  -PN -p ssh | egrep 'open'
        if [ $? -eq 0 ]
        then
          sshpass -p 'N3tG3st10n35' ssh admin@192.168.35.$n "/interface wireless monitor numbers=0 file=m192.168.35.N;tool fetch address=10.255.0.70 src-path=m192.168.35.N.txt user=dionis mode=ftp password=dionis dst-path="mo192.168.35.$n.txt" upload=yes;quit"
        else
           touch /home/dionis/mo192.168.35.$n.txt
           echo "   voltage: 0V " >> /home/dionis/mo192.168.35.$n.txt
        fi
done

for n in 20 81 112 102 170 207 175 12 195 131 166 144 91 21
do
nmap 192.168.4.$n  -PN -p ssh | egrep 'open'
        if [ $? -eq 0 ]
        then
          sshpass -p 'N3tG3st10n04' ssh admin@192.168.4.$n "/interface wireless monitor numbers=0 file=m192.168.4.N;tool fetch address=10.255.0.70 src-path=m192.168.4.N.txt user=dionis mode=ftp password=dionis dst-path="mo192.168.4.$n.txt" upload=yes;quit"
        else
           touch /home/dionis/mo192.168.4.$n.txt
           echo "   voltage: 0V " >> /home/dionis/mo192.168.4.$n.txt
        fi
done

for n in 210 35 63 211 166 149 122 171 173 126 123 96 56 172 65 145 152 32 140 19 89 50 131 79 76 61 
do
nmap 192.168.1.$n  -PN -p ssh | egrep 'open'
        if [ $? -eq 0 ]
        then
           sshpass -p 'N3tG3st10n01' ssh admin@192.168.1.$n "/interface wireless monitor numbers=0 file=m192.168.1.N;tool fetch address=10.255.0.70 src-path=m192.168.1.N.txt user=dionis mode=ftp password=dionis dst-path="mo192.168.1.$n.txt" upload=yes;quit"
        else
           touch /home/dionis/mo192.168.1.$n.txt
           echo "   voltage: 0V " >> /home/dionis/mo192.168.1.$n.txt
        fi
done


for n in 198 116 46 120 166 60 95 130 66 91 76 168 162 25 99 128 180 148 
do
nmap 192.168.9.$n  -PN -p ssh | egrep 'open'
        if [ $? -eq 0 ]
        then
           sshpass -p 'N3tG3st10n09' ssh admin@192.168.9.$n "/interface wireless monitor numbers=0 file=m192.168.9.N;tool fetch address=10.255.0.70 src-path=m192.168.9.N.txt user=dionis mode=ftp password=dionis dst-path="mo192.168.9.$n.txt" upload=yes;quit"
        else
           touch /home/dionis/mo192.168.9.$n.txt
           echo "   voltage: 0V " >> /home/dionis/mo192.168.9.$n.txt
        fi
done


python3.7 nodos.py
