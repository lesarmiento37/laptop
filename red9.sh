#!/bin/bash
rm /home/leonardo/logtest.txt
rm /home/dionis/1*

for n in {2..254}
do
sshpass -p 'N3tG3st10n09' ssh admin@192.168.9.$n "export file=192.168.9.$n;tool fetch address=10.255.0.70 src-path=192.168.9.$n.rsc user=dionis mode=ftp password=dionis dst-path="192.168.9.$n.rsc" upload=yes;quit"
sync; echo 3  > /proc/sys/vm/drop_caches
done
echo Suba2 y Tibitoc Completos;
echo Tierra Morada;

for n in {2..254}
do
sshpass -p 'N3tG3st10n35' ssh admin@192.168.35.$n "export file=192.168.35.$n;tool fetch address=10.255.0.70 src-path=192.168.35.$n.rsc user=dionis mode=ftp password=dionis dst-path="192.168.35.$n.rsc" upload=yes;quit"
sync; echo 3  > /proc/sys/vm/drop_caches
done

for n in {2..254}
do
sshpass -p 'N3tG3st10n05' ssh admin@192.168.5.$n "export file=192.168.5.$n;tool fetch address=10.255.0.70 src-path=192.168.5.$n.rsc user=dionis mode=ftp password=dionis dst-path="192.168.5.$n.rsc" upload=yes;quit"
sync; echo 3  > /proc/sys/vm/drop_caches
done

for n in {2..254}
do
sshpass -p 'N3tG3st10n04' ssh admin@192.168.4.$n "export file=192.168.4.$n;tool fetch address=10.255.0.70 src-path=192.168.4.$n.rsc user=dionis mode=ftp password=dionis dst-path="192.168.4.$n.rsc" upload=yes;quit"
sync; echo 3  > /proc/sys/vm/drop_caches
done

for n in {2..254}
do
sshpass -p 'N3tG3st10n16' ssh admin@192.168.16.$n "export file=192.168.16.$n;tool fetch address=10.255.0.70 src-path=192.168.16.$n.rsc user=dionis mode=ftp password=dionis dst-path="192.168.16.$n.rsc" upload=yes;quit"
sync; echo 3  > /proc/sys/vm/drop_caches
done

for n in {2..254}
do
sshpass -p 'N3tG3st10n19' ssh admin@192.168.19.$n "export file=192.168.19.$n;tool fetch address=10.255.0.70 src-path=192.168.19.$n.rsc user=dionis mode=ftp password=dionis dst-path="192.168.19.$n.rsc" upload=yes;quit"
sync; echo 3  > /proc/sys/vm/drop_caches
done

for n in {2..254}
do
sshpass -p 'N3tG3st10n01' ssh admin@192.168.1.$n "export file=192.168.1.$n;tool fetch address=10.255.0.70 src-path=192.168.1.$n.rsc user=dionis mode=ftp password=dionis dst-path="192.168.1.$n.rsc" upload=yes;quit"
sync; echo 3  > /proc/sys/vm/drop_caches
done

for n in {2..254}
do
sshpass -p 'N3tG3st10n21' ssh admin@192.168.21.$n "export file=192.168.21.$n;tool fetch address=10.255.0.70 src-path=192.168.21.$n.rsc user=dionis mode=ftp password=dionis dst-path="192.168.21.$n.rsc" upload=yes;quit"
sync; echo 3  > /proc/sys/vm/drop_caches
done

for ni in {2..254}
do
ping -c 1 192.168.9.$ni
if [ $? -eq 0 ] && [ ! -e "/home/dionis/192.168.9.$ni.rsc" ]
then
echo "192.168.9.$ni"
echo "192.168.9.$ni" >> /home/leonardo/logtest.txt
fi
done

for ni in {2..254}
do
ping -c 1 192.168.35.$ni
if [ $? -eq 0 ] && [ ! -e "/home/dionis/192.168.35.$ni.rsc" ]
then
echo "192.168.35.$ni"
echo "192.168.35.$ni" >> /home/leonardo/logtest.txt
fi
done

for ni in {2..254}
do
ping -c 1 192.168.5.$ni
if [ $? -eq 0 ] && [ ! -e "/home/dionis/192.168.5.$ni.rsc" ]
then
echo "192.168.5.$ni"
echo "192.168.5.$ni" >> /home/leonardo/logtest.txt
fi
done

for ni in {2..254}
do
ping -c 1 192.168.4.$ni
if [ $? -eq 0 ] && [ ! -e "/home/dionis/192.168.4.$ni.rsc" ]
then
echo "192.168.4.$ni"
echo "192.168.4.$ni" >> /home/leonardo/logtest.txt
fi
done

for ni in {2..254}
do
ping -c 1 192.168.16.$ni
if [ $? -eq 0 ] && [ ! -e "/home/dionis/192.168.16.$ni.rsc" ]
then
echo "192.168.16.$ni"
echo "192.168.16.$ni" >> /home/leonardo/logtest.txt
fi
done

for ni in {2..254}
do
ping -c 1 192.168.19.$ni
if [ $? -eq 0 ] && [ ! -e "/home/dionis/192.168.19.$ni.rsc" ]
then
echo "192.168.19.$ni"
echo "192.168.19.$ni" >> /home/leonardo/logtest.txt
fi
done

for ni in {2..254}
do
ping -c 1 192.168.1.$ni
if [ $? -eq 0 ] && [ ! -e "/home/dionis/192.168.1.$ni.rsc" ]
then
echo "192.168.1.$ni"
echo "192.168.1.$ni" >> /home/leonardo/logtest.txt
fi
done

for ni in {2..254}
do
ping -c 1 192.168.9.$ni
if [ $? -eq 0 ] && [ ! -e "/home/dionis/192.168.9.$ni.rsc" ]
then
echo "192.168.9.$ni"
echo "192.168.9.$ni" >> /home/leonardo/logtest.txt
fi
done

for ni in {2..254}
do
ping -c 1 192.168.21.$ni
if [ $? -eq 0 ] && [ ! -e "/home/dionis/192.168.21.$ni.rsc" ]
then
echo "192.168.21.$ni"
echo "192.168.21.$ni" >> /home/leonardo/logtest.txt
fi
done
