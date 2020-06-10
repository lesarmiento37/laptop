#!/usr/bin/expect -f
spawn ssh admin@192.168.9.221;
expect "admin@192.168.9.221's password:";
send "S3WAS32013\n";
expect "#";
send "cd ..\n";
expect "#";
send "cd /var/cfg\n";
send "scp config.bin leonardo@10.255.0.70:/home/leonardo\n";
expect "leonardo@10.255.0.70's password:";
send "leonardo\n";
send "\n";
expect "#";
send "exit\n";
spawn mv config.bin 192.168.9.221.bin
spawn ftp
send "open 10.255.0.20\n";
expect "Name (10.255.0.20:leonardo):";
send "NOC\n";
expect "Password:";
send "123\n";
expect "ftp>";
send "put 192.168.9.221.bin\n";
send "bye\n";
expect eof
spawn mv 192.168.9.221.bin /home/dionis/192.168.9.221.rsc

